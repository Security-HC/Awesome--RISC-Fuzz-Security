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

    data_updated = max((paper.get("last_seen", "") for paper in papers), default="")
    lines = [
        "# RISC Fuzz Security Paper Watch",
        "",
        f"Last updated: {dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()}",
        f"Data updated: {data_updated or 'No papers collected yet'}",
        "",
        "This report is generated automatically by GitHub Actions.",
        "",
