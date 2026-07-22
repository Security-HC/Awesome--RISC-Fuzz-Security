# Curation policy

This repository is a curated bibliography, not a raw keyword dump.

## Primary scope

- RISC-V and general-purpose processor fuzzing.
- Multi-hart, shared-memory, memory-consistency, and cache-coherence verification.
- Automated testing of microarchitectural security properties.
- RTL/SoC hardware fuzzing methods that are directly transferable to processor verification.
- Coverage, oracles, fuzz scheduling, bug injection, benchmarks, and artifacts used to evaluate the above.

## Default exclusions

The following are excluded unless the paper directly evaluates processor hardware, RTL, or a processor-specific oracle:

- General software, Linux-kernel, firmware, browser, network, and storage fuzzing.
- Compiler fuzzing, including RISC-V compiler testing, when no processor hardware is evaluated.
- GPU-kernel correctness and accelerator performance papers.
- Generic AI security, adversarial robustness, fraud detection, and unrelated security applications.
- Hardware synthesis, architecture performance, or hardware-Trojan papers without an automated testing/fuzzing contribution relevant to processors.

## Relevance levels

- **A — Directly relevant:** the paper directly studies processor/RISC-V fuzzing, multi-hart or memory-system verification, or microarchitectural security testing.
- **B — Strongly adjacent:** a general RTL/SoC fuzzing, oracle, formal-assistance, benchmark, or bug-injection method with direct processor applicability.
- **C — Manual review:** plausible relevance but insufficient evidence for inclusion.
- **D — Excluded:** outside scope or retrieved only because of a broad keyword collision.

## Evidence levels

- **Full-text verified:** the generated analysis used the paper text and should still be checked against the official version.
- **Abstract-level:** only title and abstract were available. Method and conclusion are explicitly marked unverified.
- **Metadata-only:** insufficient content; the record must not contain confident technical conclusions.

## Classification principles

1. Classification uses title and abstract, never the search query that happened to retrieve the record.
2. Every included paper has one primary category. Secondary matches are stored as tags; the paper is not duplicated across category reports.
3. Inclusion requires both a processor/hardware object and a testing/verification method, unless the title is in the manually curated seed list.
4. Negative and adjacent results are retained in machine-readable review/exclusion files instead of polluting the main README.

## Adding or correcting a paper

A contribution should provide the official title, date, venue/status, DOI or official page, PDF, artifact, primary category, relevance level, and a source-grounded summary. Claims about novelty, bug counts, CVEs, and evaluation improvements must be traceable to the paper or artifact.
