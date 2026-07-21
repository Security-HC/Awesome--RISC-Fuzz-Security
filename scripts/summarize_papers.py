from __future__ import annotations

import os
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
        "research_problem": abstract or "No abstract available.",
        "introduction": "Generated from metadata only. Add OPENAI_API_KEY to enable full-paper analysis.",
        "method": "Pending full-paper extraction.",
        "evaluation": "Pending full-paper extraction.",
        "conclusion": "Pending full-paper extraction.",
        "limitations": "Pending full-paper extraction.",
        "deep_reading": "Pending full-paper extraction.",
        "follow_up_questions": [
            "Is the implementation or artifact open source?",
            "Can the approach be reproduced on RISC-V cores?",
            "What oracle, coverage metric, or differential target does the paper rely on?",
        ],
        "analysis_mode": "metadata-only",
    }


def extract_pdf_text(pdf_url: str, max_pages: int = 16) -> str:
    try:
        from pypdf import PdfReader
    except Exception:
        return ""

    request = urllib.request.Request(pdf_url, headers={"User-Agent": "risc-fuzz-paper-watch/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        content = response.read()

    with tempfile.NamedTemporaryFile(suffix=".pdf") as handle:
        handle.write(content)
        handle.flush()
        reader = PdfReader(handle.name)
        pages = []
        for page in reader.pages[:max_pages]:
            pages.append(page.extract_text() or "")
    return normalize_space("\n".join(pages))[:55000]


def llm_analysis(paper: dict, full_text: str) -> dict:
    from openai import OpenAI

    model = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
    client = OpenAI()
    prompt = f"""
You are maintaining a research reading database about RISC-V, processor fuzzing,
microarchitecture security, hardware fuzzing, and verification.

Return concise JSON with these keys:
research_problem, introduction, method, evaluation, conclusion, limitations,
deep_reading, follow_up_questions.

Use Chinese for the analysis. Be specific and technical. For limitations, infer
carefully from the paper when explicit limitations are not present.

Title: {paper.get("title")}
Authors: {", ".join(paper.get("authors", []))}
Abstract: {paper.get("abstract")}

Paper text:
{full_text}
"""
    response = client.responses.create(
        model=model,
        input=prompt,
        text={"format": {"type": "json_object"}},
    )
    import json

    result = json.loads(response.output_text)
    result["analysis_mode"] = f"llm-full-text:{model}"
    return result


def needs_analysis(paper: dict) -> bool:
    analysis = paper.get("analysis") or {}
    return not all(analysis.get(field) for field in ANALYSIS_FIELDS)


def main() -> None:
    papers = read_json(DATA_DIR / "papers.json", [])
    has_key = bool(os.environ.get("OPENAI_API_KEY"))

    for paper in papers:
        if not needs_analysis(paper):
            continue
        if not has_key:
            paper["analysis"] = abstract_based_analysis(paper)
            continue
        try:
            full_text = extract_pdf_text(paper.get("pdf_url", ""))
            paper["analysis"] = llm_analysis(paper, full_text) if full_text else abstract_based_analysis(paper)
        except Exception as exc:
            paper["analysis"] = abstract_based_analysis(paper)
            paper["analysis"]["error"] = str(exc)

    write_json(DATA_DIR / "papers.json", papers)


if __name__ == "__main__":
    main()

