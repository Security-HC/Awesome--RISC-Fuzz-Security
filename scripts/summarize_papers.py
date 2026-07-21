from __future__ import annotations

import os
import json
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
    "deep_reading",
    "follow_up_questions",
]


def abstract_based_analysis(paper: dict) -> dict:
    abstract = paper.get("abstract", "")
    title = paper.get("title", "该论文")
    categories = "、".join(paper.get("categories", [])) or "未分类"
    venue = paper.get("venue") or paper.get("source") or "未记录"
    source_categories = "、".join(paper.get("source_categories", [])) or "未记录"
    matched_queries = "；".join(paper.get("matched_queries", [])[:3]) or "未记录"
    return {
        "research_problem": abstract or f"{title} 缺少可用摘要，暂时只能从标题和检索类别判断其研究问题。",
        "introduction": (
            f"该记录基于题名、摘要和元数据生成。论文来源为 {venue}，当前分类为 {categories}。"
            f"从命中查询看，论文与 {matched_queries} 相关。Introduction 部分应重点关注作者如何定义处理器/微架构/"
            "硬件 fuzzing 的验证缺口、现有方法的不足，以及本文声称的核心贡献。"
        ),
        "method": (
            "当前未进行 PDF 正文解析。可从摘要初步判断其方法线索；正式阅读时应提取 fuzz 输入生成策略、"
            "变异方式、覆盖率或反馈信号、oracle/差分对象、测试平台以及是否依赖仿真器、RTL 或真实硬件。"
        ),
        "evaluation": (
            "当前未进行 PDF 正文解析。后续应补充实验对象、baseline、发现 bug 数量、覆盖率提升、运行开销、"
            "复现条件和 artifact 可用性。"
        ),
        "conclusion": (
            "当前结论基于摘要和元数据生成：该论文可能围绕处理器安全验证、fuzzing 效率、微架构漏洞发现或硬件测试自动化展开。"
            "需要结合正文确认作者最终证明的效果和适用边界。"
        ),
        "limitations": (
            "当前未进行 PDF 正文解析。初步阅读时应重点检查：是否只覆盖特定 ISA/处理器/仿真器，是否依赖人工规则或特定 oracle，"
            "是否难以迁移到 RISC-V，是否缺少真实硬件验证，以及实验是否只在有限 benchmark 上成立。"
        ),
        "deep_reading": (
            f"元数据主题：{source_categories}。建议优先阅读 Introduction、Threat Model/Background、Method、Evaluation 和 Discussion。"
            "如果该论文与 RISC-V 或处理器 fuzzing 强相关，应进一步记录其可复用的测试生成思路、覆盖率指标、oracle 设计和开源实现。"
        ),
        "follow_up_questions": [
            "论文是否提供开源实现或实验 artifact？",
            "方法是否可以迁移到 RISC-V core、RTL 仿真器或真实处理器？",
            "论文依赖什么 oracle、覆盖率指标或差分测试对象？",
        ],
        "analysis_mode": "中文元数据分析",
        "language": "zh-CN",
    }


def extract_pdf_text(pdf_url: str, max_pages: int = 8) -> str:
    try:
        from pypdf import PdfReader
    except Exception:
        return ""

    request = urllib.request.Request(pdf_url, headers={"User-Agent": "risc-fuzz-paper-watch/1.0"})
    with urllib.request.urlopen(request, timeout=45) as response:
        content = response.read()

    with tempfile.NamedTemporaryFile(suffix=".pdf") as handle:
        handle.write(content)
        handle.flush()
        reader = PdfReader(handle.name)
        pages = []
        for page in reader.pages[:max_pages]:
            pages.append(page.extract_text() or "")
    return normalize_space("\n".join(pages))[:25000]


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
你正在维护一个中文论文阅读数据库，主题是 RISC-V、处理器 fuzzing、
微架构安全、硬件 fuzzing、RTL/SoC 验证和处理器安全。

请只返回 JSON，不要使用 Markdown 代码块。JSON 必须包含这些键：
research_problem, introduction, method, evaluation, conclusion, limitations,
deep_reading, follow_up_questions.

所有值必须使用中文。分析要具体、技术化，不要泛泛总结。
如果论文没有明确写局限性，请基于方法和实验设置谨慎推断。

论文标题：{paper.get("title")}
作者：{", ".join(paper.get("authors", []))}
摘要：{paper.get("abstract")}
分析范围：{analysis_scope}

可用文本：
{paper_text}
"""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是处理器安全、RISC-V、微架构和 fuzzing 方向的中文论文阅读助手。"},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
    )
    content = response.choices[0].message.content or "{}"
    result = parse_json_object(content)
    result["analysis_mode"] = f"{provider} 全文分析：{model}"
    result["language"] = "zh-CN"
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
    analysis = paper.get("analysis") or {}
    if analysis.get("language") != "zh-CN":
        return True
    if analysis.get("analysis_mode") == "仅元数据分析":
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
        f"待分析论文 {pending_count} 篇；"
        f"本次最多 LLM 分析 {max_llm_analyses} 篇；"
        f"PDF 全文分析 {'开启' if full_text_enabled else '关闭'}；"
        f"刷新元数据分析 {'开启' if refresh_metadata_analysis else '关闭'}；"
        f"API Key {'已配置' if has_key else '未配置'}。"
    )

    for paper in papers:
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
                analysis_scope = "PDF 前 8 页文本"
            else:
                paper_text = "\n".join(
                    [
                        f"标题：{paper.get('title', '')}",
                        f"作者：{', '.join(paper.get('authors', []))}",
                        f"摘要：{paper.get('abstract', '')}",
                        f"来源分类：{', '.join(paper.get('source_categories', []))}",
                        f"命中查询：{', '.join(paper.get('matched_queries', []))}",
                    ]
                )
                analysis_scope = "标题、摘要和元数据"
            paper["analysis"] = llm_analysis(paper, paper_text, analysis_scope) if paper_text else abstract_based_analysis(paper)
            llm_analyses_used += 1
        except Exception as exc:
            print(f"WARNING: 论文分析失败，已降级为摘要卡片：{paper.get('title', paper.get('id', 'unknown'))}\n{exc}", file=sys.stderr)
            paper["analysis"] = abstract_based_analysis(paper)
            paper["analysis"]["error"] = str(exc)

    write_json(DATA_DIR / "papers.json", papers)


if __name__ == "__main__":
    main()
