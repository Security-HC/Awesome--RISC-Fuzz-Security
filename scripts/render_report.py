from __future__ import annotations

import shutil
from collections import defaultdict

from common import DATA_DIR, REPORTS_DIR, ROOT, read_json, slugify


CATEGORY_DIRS = {
    "Multi-Hart, Memory Consistency & Cache Coherence": "multi-hart-memory-coherence",
    "RISC-V Processor Fuzzing": "risc-v-processor-fuzzing",
    "Microarchitectural Security Testing": "microarchitectural-security-testing",
    "RTL & SoC Hardware Fuzzing": "rtl-soc-hardware-fuzzing",
    "Coverage, Oracles & Fuzzing Methodology": "coverage-oracles-methodology",
    "Benchmarks, Bug Injection & Artifacts": "benchmarks-bug-injection-artifacts",
    "Formal & Directed Processor Verification": "formal-directed-verification",
}

CATEGORY_LABELS = {
    "Multi-Hart, Memory Consistency & Cache Coherence": "多 Hart、内存一致性与缓存一致性",
    "RISC-V Processor Fuzzing": "RISC-V 处理器 Fuzzing",
    "Microarchitectural Security Testing": "微架构安全自动测试",
    "RTL & SoC Hardware Fuzzing": "RTL 与 SoC 硬件 Fuzzing",
    "Coverage, Oracles & Fuzzing Methodology": "覆盖、Oracle 与 Fuzzing 方法",
    "Benchmarks, Bug Injection & Artifacts": "基准、故障注入与 Artifact",
    "Formal & Directed Processor Verification": "形式化与定向处理器验证",
}

LEGACY_DIRS = {
    "risc-v-fuzzing",
    "processor-cpu-fuzzing",
    "microarchitecture-security",
    "rtl-hardware-verification",
    "fuzzing-methodology",
    "tools-benchmarks",
    "uncategorized",
    "papers",
}


def md_escape(value: str) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def short_text(value: str, max_len: int = 150) -> str:
    value = md_escape(value)
    if len(value) <= max_len:
        return value
    return value[: max_len - 1].rstrip() + "…"


def paper_filename(paper: dict) -> str:
    year = (paper.get("published") or "unknown")[:4]
    return f"{year}-{slugify(paper.get('title', paper.get('id', 'paper')))}.md"


def category_dir(category: str) -> str:
    return CATEGORY_DIRS.get(category, slugify(category) or "other")


def category_label(category: str) -> str:
    return CATEGORY_LABELS.get(category, category)


def evidence_label(paper: dict) -> str:
    level = paper.get("evidence_level") or (paper.get("analysis") or {}).get("evidence_level") or "metadata"
    return {"full-text": "全文核验", "abstract": "摘要级", "metadata": "元数据"}.get(level, level)


def analysis_status_label(paper: dict) -> str:
    status = paper.get("analysis_status") or "unprocessed"
    labels = {
        "fulltext_verified": "已完成",
        "abstract_only": "仅摘要",
        "fulltext_pending": "等待全文",
        "fulltext_unavailable": "PDF待补",
        "fulltext_failed": "全文失败",
        "unprocessed": "未处理",
    }
    return labels.get(status, status)


def relevance_label(paper: dict) -> str:
    tier = paper.get("relevance_tier", "B")
    return {"A": "A·直接相关", "B": "B·强邻近", "C": "C·待复核", "D": "D·排除"}.get(tier, tier)


def render_detail(paper: dict) -> str:
    analysis = paper.get("analysis") or {}
    questions = analysis.get("follow_up_questions") or []
    if isinstance(questions, str):
        questions = [questions]
    question_lines = "\n".join(f"- {item}" for item in questions) or "- 暂无"
    authors = "、".join(paper.get("authors", [])) or "未记录"
    tags = "、".join(paper.get("categories", [])) or "未分类"
    reasons = "；".join(paper.get("relevance_reasons", [])) or "未记录"
    pdf_line = f"- PDF：[{paper.get('pdf_url')}]({paper.get('pdf_url')})" if paper.get("pdf_url") else "- PDF：未记录"

    return f"""# {paper.get('title', '')}

## 基本信息

- 作者：{authors}
- 发表日期：{paper.get('published', '')}
- 会议/期刊：{paper.get('venue') or paper.get('source') or '未记录'}
- 主分类：{category_label(paper.get('primary_category', ''))}
- 相关性：{relevance_label(paper)}（score={paper.get('relevance_score', '')}）
- 证据等级：{evidence_label(paper)}
- 全文状态：{analysis_status_label(paper)}
- 标签：{tags}
- 纳入依据：{reasons}
- 论文页面：[{paper.get('url', '')}]({paper.get('url', '')})
{pdf_line}
- 分析模式：{analysis.get('analysis_mode', '未知')}

## 摘要

{paper.get('abstract', '')}

## 研究问题

{analysis.get('research_problem', '')}

## Introduction 梳理

{analysis.get('introduction', '')}

## 方法

{analysis.get('method', '')}

## 实验与评估

{analysis.get('evaluation', '')}

## 核心贡献

{analysis.get('key_contribution', '')}

## 与本仓库研究主线的关系

{analysis.get('relevance_to_repo', '')}

## 结论

{analysis.get('conclusion', '')}

## 局限性

{analysis.get('limitations', '')}

## 详细阅读分析

{analysis.get('deep_reading', '')}

## 后续核验问题

{question_lines}
"""


def included_papers(papers: list[dict]) -> list[dict]:
    return [paper for paper in papers if paper.get("curation_status") == "included" or paper.get("included") is True]


def grouped_papers(papers: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for paper in included_papers(papers):
        category = paper.get("primary_category") or "Formal & Directed Processor Verification"
        grouped[category].append(paper)
    for category in grouped:
        grouped[category].sort(key=lambda item: item.get("published", ""), reverse=True)
    return grouped


def paper_link(paper: dict) -> str:
    links = [f"[页面]({paper.get('url', '')})"] if paper.get("url") else []
    if paper.get("pdf_url"):
        links.append(f"[PDF]({paper.get('pdf_url')})")
    return " / ".join(links) or "未记录"


def render_table(papers: list[dict], detail_prefix: str) -> list[str]:
    lines = [
        "| 日期 | 论文 | 会议/期刊 | 相关性 | 证据 | 核心贡献 | 链接 |",
        "|---|---|---|---|---|---|---|",
    ]
    for paper in papers:
        analysis = paper.get("analysis") or {}
        contribution = analysis.get("key_contribution") or analysis.get("conclusion") or analysis.get("research_problem") or "待核验"
        filename = paper_filename(paper)
        title = f"[{md_escape(paper.get('title', ''))}]({detail_prefix}/{filename})"
        lines.append(
            "| "
            + " | ".join(
                [
                    md_escape(paper.get("published", "")),
                    title,
                    md_escape(paper.get("venue") or paper.get("source") or "未记录"),
                    relevance_label(paper),
                    evidence_label(paper),
                    short_text(contribution),
                    paper_link(paper),
                ]
            )
            + " |"
        )
    return lines


def render_scope() -> list[str]:
    return [
        "## 收录范围",
        "",
        "本仓库不是泛化的“安全/硬件/软件 Fuzzing”抓取器，而是一个经过相关性筛选的处理器安全文献库。",
        "",
        "**核心收录：** RISC-V/处理器 Fuzzing、多 Hart 与内存一致性、缓存一致性验证、微架构安全自动测试。",
        "",
        "**强邻近收录：** 可直接迁移到处理器验证的 RTL/SoC 硬件 Fuzzing、覆盖、Oracle、形式辅助、故障注入和 Artifact。",
        "",
        "**默认排除：** 纯软件/内核/固件/编译器 Fuzzing、GPU kernel、普通 AI 安全、网络协议、存储系统及其他仅因宽泛关键词命中的论文。",
        "",
        "相关性等级：`A` 直接相关；`B` 强邻近。证据等级：`全文核验`、`摘要级`、`元数据`。摘要级记录不会被写成已经核验的确定结论。",
        "",
        "详细纳排标准见 [CURATION.md](CURATION.md)。",
        "",
    ]


def render_index(papers: list[dict], detail_prefix_mode: str = "report") -> str:
    grouped = grouped_papers(papers)
    curated = included_papers(papers)
    review = sum(1 for paper in papers if paper.get("curation_status") == "review")
    excluded = sum(1 for paper in papers if paper.get("curation_status") == "excluded")
    data_updated = max((paper.get("last_seen", "") for paper in papers), default="")
    lines = [
        "# RISC-V 处理器 Fuzzing 与安全验证文献库",
        "",
        f"数据更新日期：{data_updated or '尚未收集论文'}",
        "",
        f"当前纳入 {len(curated)} 篇；其中全文核验 {sum(1 for p in curated if (p.get('evidence_level') or (p.get('analysis') or {}).get('evidence_level')) == 'full-text')} 篇、摘要/元数据待回填 {sum(1 for p in curated if (p.get('evidence_level') or (p.get('analysis') or {}).get('evidence_level') or 'metadata') != 'full-text')} 篇；待人工复核 {review} 篇；自动排除 {excluded} 篇。",
        "",
    ]
    lines.extend(render_scope())
    lines.extend(["## 研究地图", ""])
    for category in CATEGORY_DIRS:
        category_papers = grouped.get(category, [])
        if not category_papers:
            continue
        category_path = category_dir(category)
        label = category_label(category)
        if detail_prefix_mode == "homepage":
            category_link = f"reports/{category_path}/"
            detail_prefix = f"reports/{category_path}"
        else:
            category_link = f"{category_path}/"
            detail_prefix = category_path
        lines.extend([f"### [{label}]({category_link}) · {len(category_papers)} 篇", ""])
        lines.extend(render_table(category_papers, detail_prefix))
        lines.append("")
    return "\n".join(lines)


def render_category_index(category: str, papers: list[dict]) -> str:
    label = category_label(category)
    lines = [
        f"# {label}",
        "",
        f"本目录仅按主分类收录，共 {len(papers)} 篇；论文不会因多个关键词而在多个类别中重复出现。",
        "",
        "[返回总表](../README.md)",
        "",
    ]
    lines.extend(render_table(papers, detail_prefix="."))
    lines.append("")
    return "\n".join(lines)


def render_homepage(papers: list[dict]) -> str:
    intro = [
        "# Awesome RISC-V Processor Fuzzing & Security",
        "",
        "面向 RISC-V、处理器 Fuzzing、多 Hart/内存系统验证、微架构安全自动测试与 RTL/SoC 硬件验证的**筛选式**中文文献库。",
        "",
        "机器可读数据位于 [data/papers.json](data/papers.json)；待人工复核和排除记录分别位于 `data/review_queue.json` 与 `data/excluded_papers.json`。",
        "",
    ]
    return "\n".join(intro) + "\n" + render_index(papers, detail_prefix_mode="homepage")


def render_review_queue(papers: list[dict]) -> str:
    review = [paper for paper in papers if paper.get("curation_status") == "review"]
    lines = ["# 待人工复核", "", f"共 {len(review)} 篇。该列表不进入主 README。", ""]
    lines.extend(["| 日期 | 论文 | 分数 | 自动判断依据 |", "|---|---|---:|---|"])
    for paper in review:
        reasons = "；".join(paper.get("relevance_reasons", []))
        lines.append(f"| {md_escape(paper.get('published', ''))} | [{md_escape(paper.get('title', ''))}]({paper.get('url', '')}) | {paper.get('relevance_score', '')} | {short_text(reasons, 220)} |")
    return "\n".join(lines) + "\n"


def main() -> None:
    papers = read_json(DATA_DIR / "papers.json", [])
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    for dirname in LEGACY_DIRS | set(CATEGORY_DIRS.values()) | {"review-queue"}:
        path = REPORTS_DIR / dirname
        if path.exists():
            shutil.rmtree(path)

    grouped = grouped_papers(papers)
    for category, category_papers in grouped.items():
        category_path = REPORTS_DIR / category_dir(category)
        category_path.mkdir(parents=True, exist_ok=True)
        for paper in category_papers:
            (category_path / paper_filename(paper)).write_text(render_detail(paper), encoding="utf-8")
        (category_path / "README.md").write_text(render_category_index(category, category_papers), encoding="utf-8")

    review_dir = REPORTS_DIR / "review-queue"
    review_dir.mkdir(parents=True, exist_ok=True)
    (review_dir / "README.md").write_text(render_review_queue(papers), encoding="utf-8")
    (REPORTS_DIR / "README.md").write_text(render_index(papers), encoding="utf-8")
    (ROOT / "README.md").write_text(render_homepage(papers), encoding="utf-8")


if __name__ == "__main__":
    main()
