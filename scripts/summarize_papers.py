from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import sys
import tempfile
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

from common import DATA_DIR, ROOT, normalize_space, read_json, write_json


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

FULLTEXT_VERIFIED = "fulltext_verified"
ABSTRACT_ONLY = "abstract_only"
FULLTEXT_PENDING = "fulltext_pending"
FULLTEXT_UNAVAILABLE = "fulltext_unavailable"
FULLTEXT_FAILED = "fulltext_failed"


class PdfLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        href = dict(attrs).get("href") or ""
        href_lower = href.lower()
        if ".pdf" in href_lower or "/pdf/" in href_lower or href_lower.endswith("/pdf"):
            self.links.append(href)


def abstract_based_analysis(paper: dict, reason: str = "") -> dict:
    abstract = normalize_space(paper.get("abstract", ""))
    title = paper.get("title", "该论文")
    primary_category = paper.get("primary_category") or "未分类"
    abstract_note = abstract if abstract else "当前记录没有可用摘要。"
    reason_text = f" 原因：{reason}" if reason else ""
    return {
        "research_problem": f"摘要级初步判断（未核验正文）：{abstract_note}",
        "introduction": "尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。",
        "method": "尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。",
        "evaluation": "尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。",
        "conclusion": "尚未核验正文，因此不对论文最终结论作确定性概括。",
        "limitations": "尚未核验正文。至少需要检查方法是否只适用于特定 ISA、处理器、协议、仿真器或人工模板，以及实验是否存在目标泄漏和基线不公平。",
        "key_contribution": f"待全文核验；当前仅能确认论文题名为《{title}》，初步归入“{primary_category}”。{reason_text}",
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


def normalize_pdf_candidate(url: str) -> str:
    url = (url or "").strip()
    if not url:
        return ""
    if "arxiv.org/abs/" in url:
        url = url.replace("/abs/", "/pdf/")
    if "export.arxiv.org/abs/" in url:
        url = url.replace("export.arxiv.org/abs/", "arxiv.org/pdf/")
    return url


def pdf_override_for(paper: dict, overrides: dict) -> str:
    by_id = overrides.get("by_id", {})
    by_title = overrides.get("by_title", {})
    by_doi = overrides.get("by_doi", {})
    if paper.get("id") in by_id:
        return by_id[paper["id"]]
    title_key = paper.get("title_key") or normalize_space(paper.get("title", "")).lower()
    if title_key in by_title:
        return by_title[title_key]
    doi = (paper.get("doi") or "").lower().replace("https://doi.org/", "")
    if doi and doi in by_doi:
        return by_doi[doi]
    return ""


def initial_pdf_candidates(paper: dict, overrides: dict) -> list[str]:
    candidates = [
        pdf_override_for(paper, overrides),
        paper.get("pdf_url", ""),
        paper.get("open_access_url", ""),
    ]
    source_id = paper.get("source_id", "")
    if paper.get("source") == "arXiv" and source_id:
        candidates.append(f"https://arxiv.org/pdf/{source_id}")
    url = paper.get("url", "")
    if "arxiv.org/abs/" in url:
        candidates.append(url.replace("/abs/", "/pdf/"))
    result: list[str] = []
    for value in candidates:
        value = normalize_pdf_candidate(value)
        if value and value not in result:
            result.append(value)
    return result


def discover_pdf_links(landing_url: str) -> list[str]:
    if not landing_url or not landing_url.startswith(("http://", "https://")):
        return []
    request = urllib.request.Request(
        landing_url,
        headers={"User-Agent": "Mozilla/5.0 risc-fuzz-paper-watch/3.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=35) as response:
            content_type = response.headers.get("Content-Type", "").lower()
            body = response.read(2_000_000)
            final_url = response.geturl()
    except Exception:
        return []
    if body.startswith(b"%PDF") or "application/pdf" in content_type:
        return [final_url]
    if "html" not in content_type and b"<html" not in body[:500].lower():
        return []
    parser = PdfLinkParser()
    try:
        parser.feed(body.decode("utf-8", errors="replace"))
    except Exception:
        return []
    links: list[str] = []
    for href in parser.links:
        full = urllib.parse.urljoin(final_url, href)
        if full not in links:
            links.append(full)
    return links[:12]


def download_pdf(candidates: list[str], landing_url: str = "") -> tuple[bytes, str, list[str]]:
    tried: list[str] = []
    expanded = list(candidates)
    for discovered in discover_pdf_links(landing_url):
        if discovered not in expanded:
            expanded.append(discovered)

    for candidate in expanded:
        if not candidate or candidate in tried:
            continue
        tried.append(candidate)
        # DOI landing pages are useful for link discovery, but are not themselves PDF files.
        if "doi.org/" in candidate and ".pdf" not in candidate.lower():
            for discovered in discover_pdf_links(candidate):
                if discovered not in expanded:
                    expanded.append(discovered)
            continue
        request = urllib.request.Request(
            candidate,
            headers={"User-Agent": "Mozilla/5.0 risc-fuzz-paper-watch/3.0"},
        )
        try:
            with urllib.request.urlopen(request, timeout=50) as response:
                content = response.read(50_000_000)
                content_type = response.headers.get("Content-Type", "").lower()
                final_url = response.geturl()
        except Exception:
            continue
        if content.startswith(b"%PDF") or "application/pdf" in content_type:
            return content, final_url, tried
        if "html" in content_type or b"<html" in content[:500].lower():
            parser = PdfLinkParser()
            try:
                parser.feed(content.decode("utf-8", errors="replace"))
                for href in parser.links:
                    discovered = urllib.parse.urljoin(final_url, href)
                    if discovered not in expanded:
                        expanded.append(discovered)
            except Exception:
                pass
    return b"", "", tried


def extract_pdf_text(content: bytes, max_chars: int = 100_000) -> tuple[str, int]:
    if not content:
        return "", 0
    try:
        from pypdf import PdfReader
    except Exception:
        return "", 0

    with tempfile.NamedTemporaryFile(suffix=".pdf") as handle:
        handle.write(content)
        handle.flush()
        reader = PdfReader(handle.name)
        pages: list[str] = []
        current_chars = 0
        for page in reader.pages:
            text = page.extract_text() or ""
            pages.append(text)
            current_chars += len(text)
            if current_chars >= max_chars:
                break
        total_pages = len(reader.pages)
    return normalize_space("\n".join(pages))[:max_chars], total_pages


def llm_analysis(paper: dict, paper_text: str, analysis_scope: str) -> dict:
    from openai import OpenAI

    if os.environ.get("DEEPSEEK_API_KEY"):
        model = os.environ.get("DEEPSEEK_MODEL", "deepseek-v4-flash")
        client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com", timeout=120.0)
        provider = "DeepSeek"
    else:
        model = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), timeout=120.0)
        provider = "OpenAI"

    prompt = f"""
你正在维护一个严格筛选的中文文献数据库，主题限定为：RISC-V/处理器 Fuzzing、多 hart 与内存一致性验证、微架构安全自动测试、RTL/SoC 硬件 Fuzzing，以及直接相关的覆盖、Oracle、故障注入和 Artifact。

只返回 JSON，不要使用 Markdown 代码块。必须包含：
research_problem, introduction, method, evaluation, conclusion, limitations,
key_contribution, relevance_to_repo, deep_reading, follow_up_questions, evidence_level.

要求：
1. 只依据提供的正文，不得把检索词当成论文事实。
2. 明确区分作者明确声称、实验实际证明和你的谨慎推断。
3. Introduction 概括研究缺口、既有方法不足和贡献，不复述摘要。
4. Method 必须提取输入生成、反馈/coverage、Oracle、DUT/平台、是否需要 golden model。
5. Evaluation 必须提取 baseline、实验预算、统计、bug/CVE、开销和 Artifact；正文未提供时明确写“未确认”。
6. relevance_to_repo 说明它是直接相关、强邻近还是仅方法借鉴，并指出与多 hart/一致性路径研究的关系。
7. 不得将未来工作、作者推测或摘要宣传语写成已被实验证明的结论。

论文标题：{paper.get('title')}
作者：{', '.join(paper.get('authors', []))}
主分类：{paper.get('primary_category')}
摘要：{paper.get('abstract')}
分析范围：{analysis_scope}

可用正文：
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
    result = parse_json_object(response.choices[0].message.content or "{}")
    result["analysis_mode"] = f"{provider} 全文分析：{model}；{analysis_scope}"
    result["language"] = "zh-CN"
    result["evidence_level"] = "full-text"
    return result


def parse_json_object(content: str) -> dict:
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", content, flags=re.S)
        if not match:
            raise
        return json.loads(match.group(0))


def analysis_level(paper: dict) -> str:
    analysis = paper.get("analysis") or {}
    return paper.get("evidence_level") or analysis.get("evidence_level") or "metadata"


def candidate_fingerprint(paper: dict, overrides: dict) -> str:
    values = initial_pdf_candidates(paper, overrides) + [paper.get("url", "")]
    return hashlib.sha256("|".join(values).encode("utf-8")).hexdigest()


def needs_analysis(paper: dict, overrides: dict, max_retries: int, force: bool = False) -> bool:
    if paper.get("curation_status") != "included":
        return False
    if force:
        return True
    analysis = paper.get("analysis") or {}
    if analysis_level(paper) == "full-text" and paper.get("analysis_status") == FULLTEXT_VERIFIED:
        return not all(analysis.get(field) for field in ANALYSIS_FIELDS)
    # Critical: abstract/metadata placeholders must remain in the full-text queue.
    if analysis_level(paper) in {"abstract", "metadata"}:
        previous_fingerprint = paper.get("pdf_candidate_fingerprint", "")
        current_fingerprint = candidate_fingerprint(paper, overrides)
        if previous_fingerprint and previous_fingerprint != current_fingerprint:
            return True
        attempts = int(paper.get("analysis_attempts", 0))
        return attempts < max_retries or paper.get("analysis_status") == FULLTEXT_PENDING
    return True


def priority_key(paper: dict) -> tuple:
    tier_rank = {"A": 0, "B": 1, "C": 2, "D": 3}.get(paper.get("relevance_tier", "B"), 2)
    status_rank = 0 if analysis_level(paper) in {"metadata", "abstract"} else 1
    relevance_score = -int(paper.get("relevance_score", 0) or 0)
    publication = paper.get("published", "")
    return tier_rank, status_rank, relevance_score, publication


def main() -> None:
    papers = read_json(DATA_DIR / "papers.json", [])
    overrides = read_json(ROOT / "config" / "pdf_overrides.json", {"by_id": {}, "by_title": {}, "by_doi": {}})
    has_key = bool(os.environ.get("OPENAI_API_KEY") or os.environ.get("DEEPSEEK_API_KEY"))
    max_llm_analyses = int(os.environ.get("MAX_LLM_ANALYSES_PER_RUN", "8"))
    max_retries = int(os.environ.get("MAX_FULLTEXT_RETRIES", "3"))
    full_text_enabled = os.environ.get("ENABLE_FULL_TEXT_ANALYSIS", "true").lower() == "true"
    force = os.environ.get("FORCE_FULLTEXT_REANALYSIS", "false").lower() == "true"
    today = dt.date.today().isoformat()

    pending = [paper for paper in papers if needs_analysis(paper, overrides, max_retries, force)]
    pending.sort(key=priority_key)
    print(
        "全文分析配置："
        f"纳入论文中待处理 {len(pending)} 篇；"
        f"本次最多处理 {max_llm_analyses} 篇；"
        f"PDF 全文分析 {'开启' if full_text_enabled else '关闭'}；"
        f"API Key {'已配置' if has_key else '未配置'}。"
    )

    processed = 0
    for paper in pending:
        if processed >= max_llm_analyses:
            break
        paper["analysis_last_attempt"] = today
        paper["analysis_attempts"] = int(paper.get("analysis_attempts", 0)) + 1
        paper["pdf_candidate_fingerprint"] = candidate_fingerprint(paper, overrides)

        if not has_key:
            paper["analysis"] = abstract_based_analysis(paper, "GitHub Actions 未配置 LLM API Key")
            paper["analysis_status"] = ABSTRACT_ONLY
            paper["evidence_level"] = paper["analysis"]["evidence_level"]
            processed += 1
            continue
        if not full_text_enabled:
            paper["analysis"] = abstract_based_analysis(paper, "全文分析开关未开启")
            paper["analysis_status"] = ABSTRACT_ONLY
            paper["evidence_level"] = paper["analysis"]["evidence_level"]
            processed += 1
            continue

        try:
            candidates = initial_pdf_candidates(paper, overrides)
            pdf_content, resolved_url, tried = download_pdf(candidates, paper.get("url", ""))
            if not pdf_content:
                reason = "未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL"
                paper["analysis"] = abstract_based_analysis(paper, reason)
                paper["analysis_status"] = FULLTEXT_UNAVAILABLE
                paper["fulltext_error"] = reason
                paper["fulltext_tried_urls"] = tried[-10:]
                paper["evidence_level"] = paper["analysis"]["evidence_level"]
                processed += 1
                continue

            paper_text, total_pages = extract_pdf_text(pdf_content)
            if len(paper_text) < 1500:
                reason = f"PDF 已下载但可提取文本过少（{len(paper_text)} 字符），可能是扫描版或受保护文档"
                paper["analysis"] = abstract_based_analysis(paper, reason)
                paper["analysis_status"] = FULLTEXT_FAILED
                paper["fulltext_error"] = reason
                paper["fulltext_source"] = resolved_url
                paper["evidence_level"] = paper["analysis"]["evidence_level"]
                processed += 1
                continue

            scope = f"PDF 全文共 {total_pages} 页，提取 {len(paper_text)} 字符"
            print(f"全文分析：{paper.get('title')} — {scope}")
            paper["analysis"] = llm_analysis(paper, paper_text, scope)
            paper["analysis_status"] = FULLTEXT_VERIFIED
            paper["evidence_level"] = "full-text"
            paper["fulltext_source"] = resolved_url
            paper["fulltext_text_chars"] = len(paper_text)
            paper["fulltext_pages"] = total_pages
            paper.pop("fulltext_error", None)
            processed += 1
        except Exception as exc:
            reason = f"全文下载、解析或分析失败：{exc}"
            print(f"WARNING: {paper.get('title', paper.get('id', 'unknown'))}: {reason}", file=sys.stderr)
            paper["analysis"] = abstract_based_analysis(paper, reason)
            paper["analysis_status"] = FULLTEXT_FAILED
            paper["fulltext_error"] = str(exc)
            paper["evidence_level"] = paper["analysis"]["evidence_level"]
            processed += 1

    counts: dict[str, int] = {}
    for paper in papers:
        if paper.get("curation_status") != "included":
            continue
        status = paper.get("analysis_status") or "unprocessed"
        counts[status] = counts.get(status, 0) + 1
    print(f"本次处理 {processed} 篇；纳入论文分析状态：{counts}")
    write_json(DATA_DIR / "papers.json", papers)


if __name__ == "__main__":
    main()
