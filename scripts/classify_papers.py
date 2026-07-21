from __future__ import annotations

from common import DATA_DIR, ROOT, read_json, write_json


def classify(paper: dict, rules: dict[str, list[str]]) -> list[str]:
    haystack = " ".join(
        [
            paper.get("title", ""),
            paper.get("abstract", ""),
            " ".join(paper.get("matched_queries", [])),
            " ".join(paper.get("source_categories", [])),
        ]
    ).lower()
    categories = []
    for category, keywords in rules.items():
        if any(keyword.lower() in haystack for keyword in keywords):
            categories.append(category)
    return categories or ["未分类"]


def main() -> None:
    papers = read_json(DATA_DIR / "papers.json", [])
    rules = read_json(ROOT / "config" / "categories.json", {})
    for paper in papers:
        paper["categories"] = classify(paper, rules)
    write_json(DATA_DIR / "papers.json", papers)


if __name__ == "__main__":
    main()
