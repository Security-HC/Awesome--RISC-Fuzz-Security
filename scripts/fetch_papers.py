from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET

from common import DATA_DIR, ROOT, normalize_space, read_json, slugify, write_json


ARXIV_API = "https://export.arxiv.org/api/query"
OPENALEX_API = "https://api.openalex.org/works"
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper/search"
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
            paper.get("doi", ""),
            paper.get("venue", ""),
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
    doi = paper.get("doi", "")
    if doi:
        keys.add(f"doi:{doi.lower()}")
    return keys


def abstract_from_inverted_index(index: dict | None) -> str:
    if not index:
        return ""
    words: list[tuple[int, str]] = []
    for word, positions in index.items():
        for position in positions:
            words.append((position, word))
    return normalize_space(" ".join(word for _, word in sorted(words)))


def source_display_name(work: dict) -> str:
    primary_location = work.get("primary_location") or {}
    source = primary_location.get("source") or {}
    if source.get("display_name"):
        return source["display_name"]
    host_venue = work.get("host_venue") or {}
    return host_venue.get("display_name") or ""


def openalex_pdf_url(work: dict) -> str:
    primary_location = work.get("primary_location") or {}
    if primary_location.get("pdf_url"):
        return primary_location["pdf_url"]
    open_access = work.get("open_access") or {}
    return open_access.get("oa_url") or ""


def semantic_pdf_url(paper: dict) -> str:
    open_access_pdf = paper.get("openAccessPdf") or {}
    return open_access_pdf.get("url") or ""


def semantic_external_url(paper: dict) -> str:
    external_ids = paper.get("externalIds") or {}
    if external_ids.get("DOI"):
        return f"https://doi.org/{external_ids['DOI']}"
    if paper.get("url"):
        return paper["url"]
    return ""


def is_top_venue(venue: str, top_venues: list[str]) -> bool:
    venue_key = dedupe_key(venue)
    return any(dedupe_key(item) in venue_key or venue_key in dedupe_key(item) for item in top_venues if item)


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
                "venue": "arXiv",
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


def openalex_query(search_query: str, max_results: int, from_publication_date: str, top_venues: list[str]) -> list[dict]:
    params = {
        "search": search_query,
        "per-page": max_results,
        "sort": "publication_date:desc",
        "filter": f"from_publication_date:{from_publication_date}",
    }
    url = f"{OPENALEX_API}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": "risc-fuzz-paper-watch/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace")[:1000]
        print(f"WARNING: OpenAlex query failed with HTTP {exc.code}: {search_query}\n{message}", file=sys.stderr)
        return []
    except Exception as exc:
        print(f"WARNING: OpenAlex query failed: {search_query}\n{exc}", file=sys.stderr)
        return []

    papers: list[dict] = []
    for work in payload.get("results", []):
        title = normalize_space(work.get("title") or "")
        if not title:
            continue
        venue = source_display_name(work)
        if top_venues and venue and not is_top_venue(venue, top_venues):
            continue
        work_id = work.get("id", "")
        doi = work.get("doi") or ""
        url = doi or work_id
        authors = [
            normalize_space((authorship.get("author") or {}).get("display_name", ""))
            for authorship in work.get("authorships", [])
        ]
        authors = [author for author in authors if author]
        abstract = abstract_from_inverted_index(work.get("abstract_inverted_index"))
        concepts = [
            concept.get("display_name", "")
            for concept in work.get("concepts", [])
            if concept.get("display_name")
        ]
        papers.append(
            {
                "id": f"openalex-{slugify(work_id.rsplit('/', 1)[-1])}",
                "source": "OpenAlex",
                "venue": venue or "未记录",
                "source_id": work_id,
                "doi": doi,
                "title": title,
                "title_key": dedupe_key(title),
                "authors": authors,
                "abstract": abstract,
                "published": work.get("publication_date", "") or str(work.get("publication_year", "")),
                "updated": work.get("updated_date", "")[:10],
                "url": url,
                "pdf_url": openalex_pdf_url(work),
                "source_categories": concepts,
                "matched_queries": [f"OpenAlex: {search_query}"],
                "categories": [],
                "analysis": {},
                "first_seen": dt.date.today().isoformat(),
                "last_seen": dt.date.today().isoformat(),
                "seen_count": 1,
            }
        )
    return papers


def semantic_scholar_query(search_query: str, max_results: int, from_year: int, top_venues: list[str]) -> list[dict]:
    fields = ",".join(
        [
            "title",
            "abstract",
            "year",
            "authors",
            "url",
            "venue",
            "publicationVenue",
            "externalIds",
            "openAccessPdf",
            "publicationDate",
            "fieldsOfStudy",
        ]
    )
    params = {
        "query": search_query,
        "limit": max_results,
        "fields": fields,
    }
    url = f"{SEMANTIC_SCHOLAR_API}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": "risc-fuzz-paper-watch/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace")[:1000]
        print(f"WARNING: Semantic Scholar query failed with HTTP {exc.code}: {search_query}\n{message}", file=sys.stderr)
        return []
    except Exception as exc:
        print(f"WARNING: Semantic Scholar query failed: {search_query}\n{exc}", file=sys.stderr)
        return []

    papers: list[dict] = []
    for paper in payload.get("data", []):
        title = normalize_space(paper.get("title") or "")
        if not title:
            continue
        year = int(paper.get("year") or 0)
        if year and year < from_year:
            continue
        publication_venue = paper.get("publicationVenue") or {}
        venue = publication_venue.get("name") or paper.get("venue") or ""
        if top_venues and venue and not is_top_venue(venue, top_venues):
            continue
        external_ids = paper.get("externalIds") or {}
        paper_id = paper.get("paperId") or external_ids.get("DOI") or slugify(title)
        authors = [
            normalize_space(author.get("name", ""))
            for author in paper.get("authors", [])
        ]
        authors = [author for author in authors if author]
        doi = f"https://doi.org/{external_ids['DOI']}" if external_ids.get("DOI") else ""
        papers.append(
            {
                "id": f"semantic-scholar-{slugify(paper_id)}",
                "source": "Semantic Scholar",
                "venue": venue or "未记录",
                "source_id": paper_id,
                "doi": doi,
                "title": title,
                "title_key": dedupe_key(title),
                "authors": authors,
                "abstract": normalize_space(paper.get("abstract") or ""),
                "published": paper.get("publicationDate") or str(year or ""),
                "updated": "",
                "url": semantic_external_url(paper),
                "pdf_url": semantic_pdf_url(paper),
                "source_categories": paper.get("fieldsOfStudy") or [],
                "matched_queries": [f"Semantic Scholar: {search_query}"],
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

    for field in ["title", "title_key", "authors", "abstract", "published", "updated", "url", "pdf_url", "doi", "venue", "source_categories"]:
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
    literature_queries = config.get("literature_queries", queries)
    arxiv_categories = config.get("arxiv_categories", [])
    max_results = int(config.get("max_results_per_query", 25))
    max_openalex_results = int(config.get("max_openalex_results_per_query", 25))
    max_semantic_scholar_results = int(config.get("max_semantic_scholar_results_per_query", 20))
    request_delay_seconds = int(config.get("request_delay_seconds", 10))
    openalex_from_date = config.get("openalex_from_publication_date", "2018-01-01")
    from_year = int(openalex_from_date[:4])
    top_venues = config.get("top_venues", [])

    fetched: list[dict] = []
    arxiv_count = 0
    openalex_count = 0
    semantic_scholar_count = 0
    for index, query in enumerate(queries):
        category_filter = " OR ".join(f"cat:{category}" for category in arxiv_categories)
        search_query = f"({query}) AND ({category_filter})" if category_filter else query
        results = arxiv_query(search_query, max_results)
        arxiv_count += len(results)
        fetched.extend(results)
        if index < len(queries) - 1:
            time.sleep(request_delay_seconds)

    for index, query in enumerate(literature_queries):
        results = openalex_query(query, max_openalex_results, openalex_from_date, top_venues)
        openalex_count += len(results)
        fetched.extend(results)
        if index < len(literature_queries) - 1:
            time.sleep(2)

    for index, query in enumerate(literature_queries):
        results = semantic_scholar_query(query, max_semantic_scholar_results, from_year, top_venues)
        semantic_scholar_count += len(results)
        fetched.extend(results)
        if index < len(literature_queries) - 1:
            time.sleep(2)

    print(
        "检索结果："
        f"arXiv {arxiv_count} 条；"
        f"OpenAlex {openalex_count} 条；"
        f"Semantic Scholar {semantic_scholar_count} 条；"
        f"合并前共 {len(fetched)} 条。"
    )
    existing = read_json(DATA_DIR / "papers.json", [])
    merged = merge_papers(existing, fetched)
    print(f"查重合并后共 {len(merged)} 条。")
    write_json(DATA_DIR / "papers.json", merged)


if __name__ == "__main__":
    main()
