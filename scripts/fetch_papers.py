from __future__ import annotations

import datetime as dt
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

from common import DATA_DIR, ROOT, normalize_space, read_json, slugify, write_json


ARXIV_API = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"


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
                "last_seen": dt.date.today().isoformat(),
            }
        )
    return papers


def merge_papers(existing: list[dict], fetched: list[dict]) -> list[dict]:
    by_id = {paper["id"]: paper for paper in existing}
    for paper in fetched:
        current = by_id.get(paper["id"])
        if not current:
            by_id[paper["id"]] = paper
            continue
        current_queries = set(current.get("matched_queries", []))
        current_queries.update(paper.get("matched_queries", []))
        current.update(
            {
                "title": paper["title"],
                "authors": paper["authors"],
                "abstract": paper["abstract"],
                "updated": paper["updated"],
                "url": paper["url"],
                "pdf_url": paper["pdf_url"],
                "source_categories": paper["source_categories"],
                "matched_queries": sorted(current_queries),
                "last_seen": dt.date.today().isoformat(),
            }
        )
    return sorted(by_id.values(), key=lambda item: item.get("published", ""), reverse=True)


def main() -> None:
    config = read_json(ROOT / "config" / "search_queries.json", {})
    queries = config.get("queries", [])
    arxiv_categories = config.get("arxiv_categories", [])
    max_results = int(config.get("max_results_per_query", 25))

    fetched: list[dict] = []
    for query in queries:
        category_filter = " OR ".join(f"cat:{category}" for category in arxiv_categories)
        search_query = f"({query}) AND ({category_filter})" if category_filter else query
        fetched.extend(arxiv_query(search_query, max_results))
        time.sleep(3)

    existing = read_json(DATA_DIR / "papers.json", [])
    write_json(DATA_DIR / "papers.json", merge_papers(existing, fetched))


if __name__ == "__main__":
    main()

