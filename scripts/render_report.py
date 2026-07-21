from __future__ import annotations

import shutil
from collections import defaultdict

from common import DATA_DIR, REPORTS_DIR, ROOT, slugify, read_json


CATEGORY_DIRS = {
    "RISC-V Fuzzing 研究": "risc-v-fuzzing",
    "RISC-V Fuzzing": "risc-v-fuzzing",
    "处理器与 CPU Fuzzing": "processor-cpu-fuzzing",
    "Processor and CPU Fuzzing": "processor-cpu-fuzzing",
    "微架构安全": "microarchitecture-security",
    "Microarchitecture Security": "microarchitecture-security",
    "RTL 与硬件验证": "rtl-hardware-verification",
    "RTL and Hardware Verification": "rtl-hardware-verification",
    "Fuzzing 方法论": "fuzzing-methodology",
    "Fuzzing Methodology": "fuzzing-methodology",
    "工具与基准测试": "tools-benchmarks",
    "Tools and Benchmarks": "tools-benchmarks",
    "未分类": "uncategorized",
    "Uncategorized": "uncategorized",
}

CATEGORY_LABELS = {
    "RISC-V Fuzzing": "RISC-V Fuzzing 研究",
    "Processor and CPU Fuzzing": "处理器与 CPU Fuzzing",
    "Microarchitecture Security": "微架构安全",
    "RTL and Hardware Verification": "RTL 与硬件验证",
    "Fuzzing Methodology": "Fuzzing 方法论",
    "Tools and Benchmarks": "工具与基准测试",
    "Uncategorized": "未分类",
}


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


def category_dir(category: str) -> str:
    return CATEGORY_DIRS.get(category, slugify(category) or "uncategorized")


def category_label(category: str) -> str:
    return CATEGORY_LABELS.get(category, category)


def short_text(value: str, max_len: int = 120) -> str:
    value = md_escape(value)
    if len(value) <= max_len:
        return value
    return value[: max_len - 1].rstrip() + "…"


def render_detail(paper: dict) -> str:
    analysis = paper.get("analysis") or {}
    questions = analysis.get("follow_up_questions") or []
    if isinstance(questions, str):
        questions = [questions]
    question_lines = "\n".join(f"- {item}" for item in questions)
    categories = "、".join(category_label(category) for category in paper.get("categories", [])) or "未分类"
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


def grouped_papers(papers: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for paper in papers:
        for category in paper.get("categories", ["未分类"]):
            grouped[category].append(paper)
    return grouped


def render_table(papers: list[dict], detail_prefix: str) -> list[str]:
    lines = [
        "| 发表日期 | 论文标题 | 简要研究问题 | Introduction | 方法 | 结论 | 论文页面 | PDF | 详细分析 |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for paper in papers:
        analysis = paper.get("analysis") or {}
        filename = paper_filename(paper)
        lines.append(
            "| "
            + " | ".join(
                [
                    md_escape(paper.get("published", "")),
                    md_escape(paper.get("title", "")),
                    short_text(analysis.get("research_problem", "")),
                    short_text(analysis.get("introduction", "")),
                    short_text(analysis.get("method", "")),
                    short_text(analysis.get("conclusion", "")),
                    f"[查看]({paper.get('url', '')})",
                    f"[PDF]({paper.get('pdf_url', '')})",
                    f"[阅读分析]({detail_prefix}/{filename})",
                ]
            )
            + " |"
        )
    return lines


def render_index(papers: list[dict], detail_prefix_mode: str = "report") -> str:
    grouped = grouped_papers(papers)

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
        category_path = category_dir(category)
        label = category_label(category)
        if detail_prefix_mode == "homepage":
            category_link = f"reports/{category_path}/"
            detail_prefix = f"reports/{category_path}"
        else:
            category_link = f"{category_path}/"
            detail_prefix = category_path
        lines.extend(
            [
                f"## [{label}]({category_link})",
                "",
            ]
        )
        lines.extend(render_table(grouped[category], detail_prefix=detail_prefix))
        lines.append("")
    return "\n".join(lines)


def render_category_index(category: str, papers: list[dict]) -> str:
    label = category_label(category)
    lines = [
        f"# {label}",
        "",
        f"本目录收录 `{label}` 类别下的论文，共 {len(papers)} 篇。",
        "",
        "[返回总表](../README.md)",
        "",
    ]
    lines.extend(render_table(papers, detail_prefix="."))
    lines.append("")
    return "\n".join(lines)


def render_homepage(papers: list[dict]) -> str:
    total = len(papers)
    return "\n".join(
        [
            "# Awesome--RISC-Fuzz-Security",
            "",
            "面向 RISC-V、处理器、微架构、硬件 Fuzzing 与安全验证方向的定期论文自动收集和中文阅读整理仓库。",
            "",
            f"当前已收集论文：{total} 篇。",
            "",
            "机器可读数据保存在 [data/papers.json](data/papers.json)，分类目录和完整详情页保存在 [reports/](reports/)。",
            "",
            render_index(papers, detail_prefix_mode="homepage"),
        ]
    )


def main() -> None:
    papers = read_json(DATA_DIR / "papers.json", [])
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    for old_dir in ["papers"]:
        old_path = REPORTS_DIR / old_dir
        if old_path.exists():
            shutil.rmtree(old_path)

    grouped = grouped_papers(papers)
    for category, category_papers in grouped.items():
        category_path = REPORTS_DIR / category_dir(category)
        category_path.mkdir(parents=True, exist_ok=True)
        for paper in category_papers:
            (category_path / paper_filename(paper)).write_text(render_detail(paper), encoding="utf-8")
        (category_path / "README.md").write_text(render_category_index(category, category_papers), encoding="utf-8")

    (REPORTS_DIR / "README.md").write_text(render_index(papers), encoding="utf-8")
    (ROOT / "README.md").write_text(render_homepage(papers), encoding="utf-8")


if __name__ == "__main__":
    main()
