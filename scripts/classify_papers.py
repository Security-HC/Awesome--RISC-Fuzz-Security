from __future__ import annotations

import re

from common import DATA_DIR, ROOT, normalize_space, read_json, write_json


def text_key(value: str) -> str:
    value = normalize_space(value).lower()
    value = value.replace("μ", "u")
    return re.sub(r"[^a-z0-9+.#/-]+", " ", value).strip()


def contains(text: str, phrase: str) -> bool:
    return text_key(phrase) in text


def match_rule(text: str, rule: dict) -> bool:
    any_phrases = rule.get("any_phrases", [])
    all_groups = rule.get("all_groups", [])
    if any(contains(text, phrase) for phrase in any_phrases):
        return True
    return any(all(contains(text, phrase) for phrase in group) for group in all_groups)


def evidence_level(paper: dict) -> str:
    analysis_mode = str((paper.get("analysis") or {}).get("analysis_mode", "")).lower()
    if "全文" in analysis_mode or "full-text" in analysis_mode:
        return "full-text"
    if paper.get("abstract"):
        return "abstract"
    return "metadata"


def score_relevance(paper: dict, relevance_rules: dict) -> tuple[int, str, list[str]]:
    title = text_key(paper.get("title", ""))
    abstract = text_key(paper.get("abstract", ""))
    text = f"{title} {abstract}".strip()
    reasons: list[str] = []

    manual_titles = {text_key(item) for item in relevance_rules.get("manual_include_titles", [])}
    manual_adjacent = {text_key(item) for item in relevance_rules.get("manual_adjacent_titles", [])}
    if title in manual_titles:
        return 100, "manual seed", ["manual direct seed title"]
    if title in manual_adjacent:
        return 90, "manual adjacent", ["manual adjacent seed title"]

    hard_excludes = [phrase for phrase in relevance_rules.get("hard_exclude_phrases", []) if contains(text, phrase)]
    if hard_excludes:
        return -100, "hard exclusion", [f"excluded phrase: {phrase}" for phrase in hard_excludes]

    score = 0
    title_strong = [phrase for phrase in relevance_rules.get("strong_include_phrases", []) if contains(title, phrase)]
    text_strong = [phrase for phrase in relevance_rules.get("strong_include_phrases", []) if contains(text, phrase)]
    object_hits = [term for term in relevance_rules.get("object_terms", []) if contains(text, term)]
    method_hits = [term for term in relevance_rules.get("method_terms", []) if contains(text, term)]
    security_hits = [term for term in relevance_rules.get("security_terms", []) if contains(text, term)]

    if title_strong:
        score += 5
        reasons.append("strong phrase in title: " + ", ".join(title_strong[:3]))
    elif text_strong:
        score += 3
        reasons.append("strong phrase in abstract: " + ", ".join(text_strong[:3]))

    if object_hits:
        score += 2
        reasons.append("hardware/processor object: " + ", ".join(object_hits[:4]))
    if method_hits:
        score += 2
        reasons.append("verification/fuzzing method: " + ", ".join(method_hits[:4]))
    if security_hits:
        score += 1
        reasons.append("security relevance: " + ", ".join(security_hits[:3]))

    # Relevance requires both a target hardware object and a testing/verification method.
    if not object_hits or not method_hits:
        score = min(score, 2)
        reasons.append("missing object-method conjunction")

    return score, "scored", reasons


def classify(paper: dict, category_rules: dict, relevance_rules: dict) -> dict:
    title = text_key(paper.get("title", ""))
    abstract = text_key(paper.get("abstract", ""))
    text = f"{title} {abstract}".strip()

    score, score_mode, reasons = score_relevance(paper, relevance_rules)
    min_include = int(relevance_rules.get("min_include_score", 5))
    min_review = int(relevance_rules.get("min_review_score", 3))

    matched_categories = []
    ordered_rules = sorted(
        category_rules.items(),
        key=lambda item: int((item[1] or {}).get("priority", 0)),
        reverse=True,
    )
    for category, rule in ordered_rules:
        if match_rule(text, rule or {}):
            matched_categories.append(category)

    if score >= min_include:
        core_terms = relevance_rules.get("core_scope_terms", [])
        scope = "core" if any(contains(text, term) for term in core_terms) or score_mode == "manual seed" else "adjacent"
        if score_mode == "manual adjacent":
            scope = "adjacent"
        status = "included"
        tier = "A" if scope == "core" else "B"
    elif score >= min_review:
        scope = "review"
        status = "review"
        tier = "C"
    else:
        scope = "excluded"
        status = "excluded"
        tier = "D"

    if status == "included" and not matched_categories:
        matched_categories = ["Formal & Directed Processor Verification"]

    paper["categories"] = matched_categories
    paper["primary_category"] = matched_categories[0] if matched_categories else ""
    paper["curation_status"] = status
    paper["scope"] = scope
    paper["relevance_tier"] = tier
    paper["relevance_score"] = score
    paper["relevance_reasons"] = reasons
    paper["exclusion_reason"] = "; ".join(reasons) if status == "excluded" else ""
    paper["evidence_level"] = evidence_level(paper)
    paper["included"] = status == "included"
    return paper


def main() -> None:
    papers = read_json(DATA_DIR / "papers.json", [])
    category_rules = read_json(ROOT / "config" / "categories.json", {})
    relevance_rules = read_json(ROOT / "config" / "relevance_rules.json", {})

    classified = [classify(paper, category_rules, relevance_rules) for paper in papers]
    write_json(DATA_DIR / "papers.json", classified)
    write_json(DATA_DIR / "review_queue.json", [paper for paper in classified if paper.get("curation_status") == "review"])
    write_json(DATA_DIR / "excluded_papers.json", [paper for paper in classified if paper.get("curation_status") == "excluded"])

    included = sum(1 for paper in classified if paper.get("curation_status") == "included")
    review = sum(1 for paper in classified if paper.get("curation_status") == "review")
    excluded = sum(1 for paper in classified if paper.get("curation_status") == "excluded")
    print(f"分类结果：纳入 {included} 篇；待人工复核 {review} 篇；排除 {excluded} 篇。")


if __name__ == "__main__":
    main()
