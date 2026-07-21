from __future__ import annotations

import datetime as dt
import hashlib
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET

from common import DATA_DIR, ROOT, normalize_space, read_json, slugify, write_json


ARXIV_API = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"


def dedupe_key(value: str) -> str:
    value = normalize_space(value).lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return normalize_space(value)


def content_hash(paper: dict) -> str:
    relevant = "|".join(
        [
            paper.get("title", ""),
            " ".join(paper.get("authors", [])),
            paper.get("abstract", ""),
            paper.get("published", ""),
            paper.get("updated", ""),
            paper.get("url", ""),
            paper.get("pdf_url", ""),
            " ".join(paper.get("source_categories", [])),
        ]
    )
    return hashlib.sha256(relevant.encode("utf-8")).hexdigest()


def index_keys(paper: dict) -> set[str]:
    keys = {f"id:{paper.get('id', '')}"}
    source = paper.get("source", "")
    source_id = paper.get("source_id", "")
    if source and source_id:
        keys.add(f"source:{source}:{source_id}")
    title_key = paper.get("title_key") or dedupe_key(paper.get("title", ""))
    if title_key:
        keys.add(f"title:{title_key}")
    pdf_url = paper.get("pdf_url", "")
    if pdf_url:
        keys.add(f"pdf:{pdf_url}")
    url = paper.get("url", "")
    if url:
        keys.add(f"url:{url}")
    return keys


def arxiv_query(search_query: str, max_results: int) -> list[dict]:
    params = {
        "search_query": search_query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": "risc-fuzz-paper-watch/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            body = response.read()
    except urllib.error.HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace")[:1000]
        print(f"WARNING: arXiv query failed with HTTP {exc.code}: {search_query}\n{message}", file=sys.stderr)
        return []
    except Exception as exc:
        print(f"WARNING: arXiv query failed: {search_query}\n{exc}", file=sys.stderr)
        return []

    try:
        root = ET.fromstring(body)
    except ET.ParseError as exc:
        print(f"WARNING: arXiv response parse failed: {search_query}\n{exc}", file=sys.stderr)
        return []
    papers: list[dict] = []
    for entry in root.findall(f"{ATOM}entry"):
        paper_url = entry.findtext(f"{ATOM}id", default="")
        arxiv_id = paper_url.rsplit("/", 1)[-1]
        title = normalize_space(entry.findtext(f"{ATOM}title", default=""))
        abstract = normalize_space(entry.findtext(f"{ATOM}summary", default=""))
        published_raw = entry.findtext(f"{ATOM}published", default="")
        updated_raw = entry.findtext(f"{ATOM}updated", default="")
        authors = [
            normalize_space(author.findtext(f"{ATOM}name", default=""))
            for author in entry.findall(f"{ATOM}author")
        ]
        categories = [node.attrib.get("term", "") for node in entry.findall(f"{ATOM}category")]
        pdf_url = ""
        for link in entry.findall(f"{ATOM}link"):
            if link.attrib.get("title") == "pdf" or link.attrib.get("type") == "application/pdf":
                pdf_url = link.attrib.get("href", "")

        papers.append(
            {
                "id": f"arxiv-{slugify(arxiv_id)}",
                "source": "arXiv",
                "source_id": arxiv_id,
                "title": title,
                "title_key": dedupe_key(title),
                "authors": authors,
                "abstract": abstract,
                "published": published_raw[:10],
                "updated": updated_raw[:10],
                "url": paper_url,
                "pdf_url": pdf_url or paper_url.replace("/abs/", "/pdf/"),
                "source_categories": categories,
                "matched_queries": [search_query],
                "categories": [],
                "analysis": {},
                "first_seen": dt.date.today().isoformat(),
                "last_seen": dt.date.today().isoformat(),
                "seen_count": 1,
            }
        )
    return papers


def add_to_index(index: dict[str, str], paper: dict) -> None:
    for key in index_keys(paper):
        if key.endswith(":"):
            continue
        index[key] = paper["id"]


def merge_into_current(current: dict, paper: dict, today: str) -> bool:
    changed = False

    current_queries = set(current.get("matched_queries", []))
    incoming_queries = set(paper.get("matched_queries", []))
    merged_queries = sorted(current_queries | incoming_queries)
    if merged_queries != current.get("matched_queries", []):
        current["matched_queries"] = merged_queries
        changed = True

    for field in ["title", "title_key", "authors", "abstract", "published", "updated", "url", "pdf_url", "source_categories"]:
        incoming = paper.get(field)
        if incoming and current.get(field) != incoming:
            current[field] = incoming
            changed = True

    if not current.get("first_seen"):
        current["first_seen"] = current.get("last_seen") or today
        changed = True

    if changed:
        current["last_seen"] = today
        current["seen_count"] = int(current.get("seen_count", 1)) + 1
        current["content_hash"] = content_hash(current)
    else:
        current.setdefault("seen_count", 1)
        current.setdefault("first_seen", current.get("last_seen") or today)
        current.setdefault("last_seen", current.get("first_seen") or today)
        current.setdefault("content_hash", content_hash(current))
    return changed


def merge_papers(existing: list[dict], fetched: list[dict]) -> list[dict]:
    today = dt.date.today().isoformat()
    by_id = {paper["id"]: paper for paper in existing}
    key_index: dict[str, str] = {}
    for paper in by_id.values():
        paper.setdefault("title_key", dedupe_key(paper.get("title", "")))
        paper.setdefault("first_seen", paper.get("last_seen") or today)
        paper.setdefault("seen_count", 1)
        paper.setdefault("content_hash", content_hash(paper))
        add_to_index(key_index, paper)

    for paper in fetched:
        paper["content_hash"] = content_hash(paper)
        matched_id = next((key_index[key] for key in index_keys(paper) if key in key_index), "")
        current = by_id.get(matched_id or paper["id"])
        if not current:
            by_id[paper["id"]] = paper
            add_to_index(key_index, paper)
            continue
        merge_into_current(current, paper, today)
        add_to_index(key_index, current)
    return sorted(by_id.values(), key=lambda item: item.get("published", ""), reverse=True)


def main() -> None:
    config = read_json(ROOT / "config" / "search_queries.json", {})
    queries = config.get("queries", [])
    arxiv_categories = config.get("arxiv_categories", [])
    max_results = int(config.get("max_results_per_query", 25))
    request_delay_seconds = int(config.get("request_delay_seconds", 10))

    fetched: list[dict] = []
    for index, query in enumerate(queries):
        category_filter = " OR ".join(f"cat:{category}" for category in arxiv_categories)
        search_query = f"({query}) AND ({category_filter})" if category_filter else query
        fetched.extend(arxiv_query(search_query, max_results))
        if index < len(queries) - 1:
            time.sleep(request_delay_seconds)

    existing = read_json(DATA_DIR / "papers.json", [])
    write_json(DATA_DIR / "papers.json", merge_papers(existing, fetched))


if __name__ == "__main__":
    main()
