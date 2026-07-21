from __future__ import annotations

from collections import defaultdict

from common import DATA_DIR, PAPER_REPORTS_DIR, REPORTS_DIR, slugify, read_json


def md_escape(value: str) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def authors_short(authors: list[str]) -> str:
    if not authors:
        return "未记录"
    if len(authors) <= 3:
        return ", ".join(authors)
    return f"{', '.join(authors[:3])} 等"


def paper_filename(paper: dict) -> str:
    year = (paper.get("published") or "unknown")[:4]
    return f"{year}-{slugify(paper.get('title', paper.get('id', 'paper')))}.md"


def render_detail(paper: dict) -> str:
    analysis = paper.get("analysis") or {}
    questions = analysis.get("follow_up_questions") or []
    if isinstance(questions, str):
        questions = [questions]
    question_lines = "\n".join(f"- {item}" for item in questions)
    categories = "、".join(paper.get("categories", [])) or "未分类"
    authors = "、".join(paper.get("authors", [])) or "未记录"
    first_seen = paper.get("first_seen", "")
    last_seen = paper.get("last_seen", "")
    seen_count = paper.get("seen_count", "")

    return f"""# {paper.get("title", "")}

## 基本信息

- 作者：{authors}
- 发表日期：{paper.get("published", "")}
- 更新日期：{paper.get("updated", "")}
- 来源：{paper.get("source", "")}
- 来源编号：{paper.get("source_id", "")}
- 研究类别：{categories}
- 首次发现：{first_seen}
- 最近更新：{last_seen}
- 命中次数：{seen_count}
- 论文页面：[{paper.get("url", "")}]({paper.get("url", "")})
- PDF：[{paper.get("pdf_url", "")}]({paper.get("pdf_url", "")})
- 分析模式：{analysis.get("analysis_mode", "未知")}

## 摘要

{paper.get("abstract", "")}

## 研究问题

{analysis.get("research_problem", "")}

## Introduction 梳理

{analysis.get("introduction", "")}

## 方法

{analysis.get("method", "")}

## 实验与评估

{analysis.get("evaluation", "")}

## 结论

{analysis.get("conclusion", "")}

## 局限性

{analysis.get("limitations", "")}

## 详细阅读分析

{analysis.get("deep_reading", "")}

## 后续跟进问题

{question_lines}
"""


def render_index(papers: list[dict]) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for paper in papers:
        for category in paper.get("categories", ["未分类"]):
            grouped[category].append(paper)

    data_updated = max((paper.get("last_seen", "") for paper in papers), default="")
    lines = [
        "# RISC/处理器 Fuzzing 与安全论文观察",
        "",
        f"数据更新日期：{data_updated or '尚未收集论文'}",
        "",
        "本报告由 GitHub Actions 自动生成，按研究类别整理 RISC-V、处理器、微架构、硬件 fuzzing 与安全验证相关论文。",
        "",
    ]

    for category in sorted(grouped):
        lines.extend(
            [
                f"## {category}",
                "",
                "| 发表日期 | 论文标题 | 作者 | 来源 | 命中关键词 | 论文页面 | PDF | 详细分析 |",
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
                        f"[查看]({paper.get('url', '')})",
                        f"[PDF]({paper.get('pdf_url', '')})",
                        f"[阅读分析](papers/{filename})",
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
