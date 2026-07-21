from __future__ import annotations

import datetime as dt
from collections import defaultdict

from common import DATA_DIR, PAPER_REPORTS_DIR, REPORTS_DIR, slugify, read_json


def md_escape(value: str) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def authors_short(authors: list[str]) -> str:
    if not authors:
        return ""
    if len(authors) <= 3:
        return ", ".join(authors)
    return f"{', '.join(authors[:3])}, et al."


def paper_filename(paper: dict) -> str:
    year = (paper.get("published") or "unknown")[:4]
    return f"{year}-{slugify(paper.get('title', paper.get('id', 'paper')))}.md"


def render_detail(paper: dict) -> str:
    analysis = paper.get("analysis") or {}
    questions = analysis.get("follow_up_questions") or []
    if isinstance(questions, str):
        questions = [questions]
    question_lines = "\n".join(f"- {item}" for item in questions)
    categories = ", ".join(paper.get("categories", []))
    authors = ", ".join(paper.get("authors", []))

    return f"""# {paper.get("title", "")}

## Basic Information

- Authors: {authors}
- Published: {paper.get("published", "")}
- Updated: {paper.get("updated", "")}
- Source: {paper.get("source", "")}
- Source ID: {paper.get("source_id", "")}
- Categories: {categories}
- Paper: [{paper.get("url", "")}]({paper.get("url", "")})
- PDF: [{paper.get("pdf_url", "")}]({paper.get("pdf_url", "")})
- Analysis mode: {analysis.get("analysis_mode", "unknown")}

## Abstract

{paper.get("abstract", "")}

## Research Problem

{analysis.get("research_problem", "")}

## Introduction

{analysis.get("introduction", "")}

## Method

{analysis.get("method", "")}

## Evaluation

{analysis.get("evaluation", "")}

## Conclusion

{analysis.get("conclusion", "")}

## Limitations

{analysis.get("limitations", "")}

## Detailed Reading Analysis

{analysis.get("deep_reading", "")}

## Follow-up Questions

{question_lines}
"""


def render_index(papers: list[dict]) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for paper in papers:
        for category in paper.get("categories", ["Uncategorized"]):
            grouped[category].append(paper)

    lines = [
        "# RISC Fuzz Security Paper Watch",
        "",
        f"Last updated: {dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()}",
        "",
        "This report is generated automatically by GitHub Actions.",
        "",
    ]

    for category in sorted(grouped):
        lines.extend(
            [
                f"## {category}",
                "",
                "| Published | Title | Authors | Source | Keywords | Paper | PDF | Analysis |",
                "|---|---|---|---|---|---|---|---|",
            ]
        )
        for paper in grouped[category]:
            filename = paper_filename(paper)
            queries = ", ".join(paper.get("matched_queries", [])[:3])
            lines.append(
                "| "
                + " | ".join(
                    [
                        md_escape(paper.get("published", "")),
                        md_escape(paper.get("title", "")),
                        md_escape(authors_short(paper.get("authors", []))),
                        md_escape(paper.get("source", "")),
                        md_escape(queries),
                        f"[Link]({paper.get('url', '')})",
                        f"[PDF]({paper.get('pdf_url', '')})",
                        f"[Details](papers/{filename})",
                    ]
                )
                + " |"
            )
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    papers = read_json(DATA_DIR / "papers.json", [])
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    PAPER_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    for paper in papers:
        (PAPER_REPORTS_DIR / paper_filename(paper)).write_text(render_detail(paper), encoding="utf-8")

    (REPORTS_DIR / "README.md").write_text(render_index(papers), encoding="utf-8")


if __name__ == "__main__":
    main()
