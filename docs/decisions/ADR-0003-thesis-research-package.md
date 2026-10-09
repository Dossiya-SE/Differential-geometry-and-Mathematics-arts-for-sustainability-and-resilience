# ADR-0003 — Add an application-specific thesis research package without changing the domain-neutral core

- Status: `PROPOSED`
- Date: `2026-08-31`

## Context

The repository was intentionally established as a domain-neutral research platform. A substantial thesis-design session has now produced two tightly related P–W–T application trajectories:

1. **Graph-to-Viability Geometry of Sustainable and Resilient Power–Water–Transportation Systems**;
2. **Differential and Nonsmooth Geometry of Sustainable Infrastructure Viability**.

The second trajectory is currently the stronger candidate for a long-term mathematics-specialization path, but the research-gap and novelty claims remain evidence-bounded and require systematic-review closure.

## Decision

Create `docs/thesis/` as an application-specific research package while preserving the repository-level domain-neutral architecture.

The thesis package may define P–W–T systems, sustainability constraints, viability sets, Riemannian metrics, nonsmooth geometry, research questions, hypotheses, industrial integration hypotheses, presentation specifications, and exploratory extensions.

It must not silently change platform-wide assumptions or treat candidate gaps as validated novelty.

## Consequences

- `docs/index.qmd` will link to the thesis package.
- `docs/thesis/` uses the evidence states defined in `docs/RESEARCH_INTEGRITY.md`.
- Application-specific equations, assumptions, and candidate claims are isolated from domain-neutral platform contracts until separately adopted.
- A future decision record is required before any thesis title or application boundary is declared repository-wide `FROZEN` or `VALIDATED`.

