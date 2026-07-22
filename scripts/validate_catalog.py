from __future__ import annotations

from collections import Counter

from common import DATA_DIR, ROOT, read_json


def main() -> None:
    papers = read_json(DATA_DIR / "papers.json", [])
    included = [paper for paper in papers if paper.get("curation_status") == "included"]
    review = [paper for paper in papers if paper.get("curation_status") == "review"]
    excluded = [paper for paper in papers if paper.get("curation_status") == "excluded"]

    errors: list[str] = []
    for paper in included:
        if not paper.get("primary_category"):
            errors.append(f"included paper missing primary_category: {paper.get('title')}")
        if paper.get("relevance_tier") not in {"A", "B"}:
            errors.append(f"included paper has invalid tier: {paper.get('title')}")

    title_counts = Counter((paper.get("title_key") or paper.get("title", "").lower()) for paper in included)
    duplicates = [title for title, count in title_counts.items() if title and count > 1]
    if duplicates:
        errors.append("duplicate included titles: " + ", ".join(duplicates[:10]))

    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    forbidden = ["cotton fiber", "digital fraud", "autonomous vehicle", "sparse matrix"]
    for phrase in forbidden:
        if phrase.lower() in readme.lower():
            errors.append(f"excluded topic leaked into README: {phrase}")

    print(f"Catalog validation: included={len(included)}, review={len(review)}, excluded={len(excluded)}")
    if errors:
        raise SystemExit("\n".join(errors))


if __name__ == "__main__":
    main()
