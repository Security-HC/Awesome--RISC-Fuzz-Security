from __future__ import annotations

import json
import os
import re
import sys
import tempfile
import urllib.request

from common import DATA_DIR, normalize_space, read_json, write_json


ANALYSIS_FIELDS = [
    "research_problem",
    "introduction",
    "method",
    "evaluation",
    "conclusion",
    "limitations",
    "key_contribution",
    "relevance_to_repo",
    "deep_reading",
    "follow_up_questions",
]


def abstract_based_analysis(paper: dict) -> dict:
    abstract = normalize_space(paper.get("abstract", ""))
    title = paper.get("title", "该论文")
    primary_category = paper.get("primary_category") or "未分类"
    abstract_note = abstract if abstract else "当前记录没有可用摘要。"
    return {
        "research_problem": f"摘要级初步判断（未核验正文）：{abstract_note}",
        "introduction": "尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。",
        "method": "尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。",
        "evaluation": "尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。",
        "conclusion": "尚未核验正文，因此不对论文最终结论作确定性概括。",
        "limitations": "尚未核验正文。至少需要检查方法是否只适用于特定 ISA、处理器、协议、仿真器或人工模板，以及实验是否存在目标泄漏和基线不公平。",
        "key_contribution": f"待全文核验；当前仅能确认论文题名为《{title}》，初步归入“{primary_category}”。",
        "relevance_to_repo": "该条目已通过自动相关性筛选，但尚未完成人工或全文级核验。",
        "deep_reading": "优先阅读 Introduction、Background/Threat Model、Method、Evaluation、Limitations/Discussion，并核对官方论文页、DOI、Artifact 和代码仓库。",
        "follow_up_questions": [
            "论文的在线反馈信号和最终 Oracle 分别是什么？",
            "实验是否包含公平的 random、通用 RTL coverage 和领域专用 coverage 基线？",
            "论文是否提供开源 Artifact、真实漏洞、CVE 或可复现 PoC？",
        ],
        "analysis_mode": "摘要级占位（未全文核验）",
        "evidence_level": "abstract" if abstract else "metadata",
        "language": "zh-CN",
    }


def extract_pdf_text(pdf_url: str, max_first_pages: int = 8, max_last_pages: int = 2) -> str:
    if not pdf_url:
        return ""
    try:
        from pypdf import PdfReader
    except Exception:
        return ""

    request = urllib.request.Request(pdf_url, headers={"User-Agent": "risc-fuzz-paper-watch/2.0"})
    with urllib.request.urlopen(request, timeout=45) as response:
        content = response.read()

    with tempfile.NamedTemporaryFile(suffix=".pdf") as handle:
        handle.write(content)
        handle.flush()
        reader = PdfReader(handle.name)
        total = len(reader.pages)
        indexes = list(range(min(max_first_pages, total)))
        if total > max_first_pages:
            indexes.extend(range(max(max_first_pages, total - max_last_pages), total))
        pages = [(reader.pages[index].extract_text() or "") for index in dict.fromkeys(indexes)]
    return normalize_space("\n".join(pages))[:50000]


def llm_analysis(paper: dict, paper_text: str, analysis_scope: str) -> dict:
    from openai import OpenAI

    if os.environ.get("DEEPSEEK_API_KEY"):
        model = os.environ.get("DEEPSEEK_MODEL", "deepseek-v4-flash")
        client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com", timeout=90.0)
        provider = "DeepSeek"
    else:
        model = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), timeout=90.0)
        provider = "OpenAI"

    prompt = f"""
你正在维护一个严格筛选的中文文献数据库，主题限定为：RISC-V/处理器 Fuzzing、多 hart 与内存一致性验证、微架构安全自动测试、RTL/SoC 硬件 Fuzzing，以及直接相关的覆盖、Oracle、故障注入和 Artifact。

只返回 JSON，不要使用 Markdown 代码块。必须包含：
research_problem, introduction, method, evaluation, conclusion, limitations,
key_contribution, relevance_to_repo, deep_reading, follow_up_questions, evidence_level.

要求：
1. 只依据提供的正文/摘要，不得把检索词当成论文事实。
2. 明确区分作者明确声称、实验实际证明和你的谨慎推断。
3. Introduction 应概括研究缺口、既有方法不足和贡献，不要复述摘要。
4. Method 必须提取输入生成、反馈/coverage、Oracle、DUT/平台、是否需要 golden model。
5. Evaluation 必须提取 baseline、实验预算、统计、bug/CVE、开销和 Artifact；正文未提供时明确写“未确认”。
6. relevance_to_repo 必须说明它是直接相关、强邻近还是仅方法借鉴，并指出与多 hart/一致性路径研究的关系。
7. 如果文本只覆盖论文前几页，结论和局限必须标记证据不足。

论文标题：{paper.get('title')}
作者：{', '.join(paper.get('authors', []))}
主分类：{paper.get('primary_category')}
摘要：{paper.get('abstract')}
分析范围：{analysis_scope}

可用文本：
{paper_text}
"""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是处理器验证、RISC-V、微架构安全和硬件 Fuzzing 方向的严谨文献审稿助手。"},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
    )
    content = response.choices[0].message.content or "{}"
    result = parse_json_object(content)
    result["analysis_mode"] = f"{provider} {analysis_scope}：{model}"
    result["language"] = "zh-CN"
    result.setdefault("evidence_level", "full-text" if "PDF" in analysis_scope else "abstract")
    return result


def parse_json_object(content: str) -> dict:
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", content, flags=re.S)
        if not match:
            raise
        return json.loads(match.group(0))


def needs_analysis(paper: dict) -> bool:
    if paper.get("curation_status") != "included":
        return False
    analysis = paper.get("analysis") or {}
    if analysis.get("language") != "zh-CN":
        return True
    if analysis.get("analysis_mode") in {"仅元数据分析", "中文元数据分析"}:
        return True
    return not all(analysis.get(field) for field in ANALYSIS_FIELDS)


def main() -> None:
    papers = read_json(DATA_DIR / "papers.json", [])
    has_key = bool(os.environ.get("OPENAI_API_KEY") or os.environ.get("DEEPSEEK_API_KEY"))
    max_llm_analyses = int(os.environ.get("MAX_LLM_ANALYSES_PER_RUN", "5"))
    full_text_enabled = os.environ.get("ENABLE_FULL_TEXT_ANALYSIS", "false").lower() == "true"
    refresh_metadata_analysis = os.environ.get("REFRESH_METADATA_ANALYSIS", "false").lower() == "true"
    llm_analyses_used = 0
    pending_count = sum(1 for paper in papers if needs_analysis(paper))
    print(
        "摘要配置："
        f"纳入论文中待分析 {pending_count} 篇；"
        f"本次最多 LLM 分析 {max_llm_analyses} 篇；"
        f"PDF 全文分析 {'开启' if full_text_enabled else '关闭'}；"
        f"API Key {'已配置' if has_key else '未配置'}。"
    )

    for paper in papers:
        if paper.get("curation_status") != "included":
            continue
        if not needs_analysis(paper) and not refresh_metadata_analysis:
            continue
        if not has_key:
            paper["analysis"] = abstract_based_analysis(paper)
            continue
        if llm_analyses_used >= max_llm_analyses:
            if not paper.get("analysis"):
                paper["analysis"] = abstract_based_analysis(paper)
            continue
        try:
            print(f"分析论文：{paper.get('title', paper.get('id', 'unknown'))}")
            if full_text_enabled:
                paper_text = extract_pdf_text(paper.get("pdf_url", ""))
                analysis_scope = "PDF 首 8 页与末 2 页文本"
            else:
                paper_text = "\n".join(
                    [
                        f"标题：{paper.get('title', '')}",
                        f"作者：{', '.join(paper.get('authors', []))}",
                        f"摘要：{paper.get('abstract', '')}",
                    ]
                )
                analysis_scope = "标题与摘要"
            paper["analysis"] = llm_analysis(paper, paper_text, analysis_scope) if paper_text else abstract_based_analysis(paper)
            llm_analyses_used += 1
        except Exception as exc:
            print(f"WARNING: 论文分析失败，降级为摘要占位：{paper.get('title', paper.get('id', 'unknown'))}\n{exc}", file=sys.stderr)
            paper["analysis"] = abstract_based_analysis(paper)
            paper["analysis"]["error"] = str(exc)

    write_json(DATA_DIR / "papers.json", papers)


if __name__ == "__main__":
    main()
