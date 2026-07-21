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
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": "risc-fuzz-paper-watch/1.0"})
    with urllib.request.urlopen(request, timeout=45) as response:
        body = response.read()

    root = ET.fromstring(body)
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
