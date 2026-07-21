# Awesome--RISC-Fuzz-Security

Daily paper radar for RISC-V, processor, microarchitecture, hardware fuzzing, and security verification research.

## What It Builds

The GitHub Action runs every day and updates:

- [reports/README.md](reports/README.md): category-based paper table
- `reports/papers/*.md`: detailed reading notes for each paper
- [data/papers.json](data/papers.json): accumulated paper metadata and analysis state

Each detailed note tracks:

- Basic metadata and clickable paper links
- Research problem
- Introduction summary
- Method
- Evaluation
- Conclusion
- Limitations
- Deeper reading analysis
- Follow-up research questions

## Daily Schedule

The workflow is configured for 09:00 Beijing time every day:

```yaml
cron: "0 1 * * *"
```

GitHub Actions cron uses UTC, so `01:00 UTC` is `09:00 Asia/Shanghai`.

You can also run it manually from the GitHub Actions tab with `workflow_dispatch`.

## Required Repository Secret

For full-paper LLM analysis, add this repository secret:

```text
OPENAI_API_KEY
```

Without the secret, the workflow still fetches papers and creates metadata-based notes from titles and abstracts.

## Search Scope

The default search includes:

- RISC-V fuzzing
- processor fuzzing
- CPU fuzzing
- microarchitecture fuzzing
- hardware fuzzing
- ISA testing
- instruction set fuzzing
- RTL fuzzing
- SoC verification
- transient execution fuzzing
- cache side channel fuzzing

Edit [config/search_queries.json](config/search_queries.json) and [config/categories.json](config/categories.json) to tune keywords and categories.

## Deduplication

The collector deduplicates papers before rendering reports. A paper is treated as already known when any of these match an existing record:

- arXiv/source ID
- Normalized title
- Abstract page URL
- PDF URL

Existing papers are not rewritten every day when nothing changed, so the scheduled Action should not create noisy commits for the same search results. The metadata keeps `first_seen`, `last_seen`, `seen_count`, and `content_hash` fields for traceability.
