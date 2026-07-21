from __future__ import annotations

import datetime as dt
import hashlib
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

from common import DATA_DIR, ROOT, normalize_space, read_json, slugify, write_json


ARXIV_API = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"


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
                "source": "arXiv",
                "source_id": arxiv_id,
                "title": title,
                "title_key": dedupe_key(title),
                "authors": authors,
                "abstract": abstract,
                "published": published_raw[:10],
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
