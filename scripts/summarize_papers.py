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
    return {
        "research_problem": abstract or "暂无摘要信息。",
        "introduction": "当前为基于题名和摘要生成的记录。配置 OPENAI_API_KEY 或 DEEPSEEK_API_KEY 后，可以启用全文阅读分析。",
        "method": "等待全文提取后补充。",
        "evaluation": "等待全文提取后补充。",
        "conclusion": "等待全文提取后补充。",
        "limitations": "等待全文提取后补充。初步阅读时应重点检查适用架构、测试对象、oracle 设计、覆盖率指标和复现实验条件。",
        "deep_reading": "等待全文提取后补充。建议结合论文 PDF、开源 artifact、实验对象和可迁移到 RISC-V/处理器 fuzzing 的部分继续分析。",
        "follow_up_questions": [
            "论文是否提供开源实现或实验 artifact？",
            "方法是否可以迁移到 RISC-V core、RTL 仿真器或真实处理器？",
            "论文依赖什么 oracle、覆盖率指标或差分测试对象？",
        ],
        "analysis_mode": "仅元数据分析",
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
    return normalize_space("\n".join(pages))[:55000]
    return normalize_space("\n".join(pages))[:25000]


def llm_analysis(paper: dict, full_text: str) -> dict:
    from openai import OpenAI

    if os.environ.get("DEEPSEEK_API_KEY"):
        model = os.environ.get("DEEPSEEK_MODEL", "deepseek-v4-flash")
        client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com")
        client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com", timeout=90.0)
        provider = "DeepSeek"
    else:
        model = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
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

论文正文：
{full_text}
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
    return not all(analysis.get(field) for field in ANALYSIS_FIELDS)


def main() -> None:
    papers = read_json(DATA_DIR / "papers.json", [])
    has_key = bool(os.environ.get("OPENAI_API_KEY") or os.environ.get("DEEPSEEK_API_KEY"))
    max_llm_analyses = int(os.environ.get("MAX_LLM_ANALYSES_PER_RUN", "5"))
    llm_analyses_used = 0

    for paper in papers:
        if not needs_analysis(paper):
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
            full_text = extract_pdf_text(paper.get("pdf_url", ""))
            paper["analysis"] = llm_analysis(paper, full_text) if full_text else abstract_based_analysis(paper)
            llm_analyses_used += 1
        except Exception as exc:
            print(f"WARNING: 论文分析失败，已降级为摘要卡片：{paper.get('title', paper.get('id', 'unknown'))}\n{exc}", file=sys.stderr)
            paper["analysis"] = abstract_based_analysis(paper)
            paper["analysis"]["error"] = str(exc)

    write_json(DATA_DIR / "papers.json", papers)


if __name__ == "__main__":
    main()
