# ADR-0004 — Admit a governed Chapter 10 educational skill and experimental renderer

- Date: 2026-10-09
- Status: **PROPOSED** (not an approved research stochastic model)
- Application/hazard/system boundary/outcomes: **NOT_SELECTED**
- Traces: `MSR-SKILL-SR-001` and `MSR-FIG-0003`
- Reference: Gonzalez Vivo and Lowe, *The Book of Shaders*, Chapter 10 (conceptual learning only)

## Decision

1. Add a repository-local `SKILL.md` organized around independently written teaching code, mathematics, tests, task-specific adaptation, and falsification criteria.
2. Reuse the existing WebGL2 + dependency-free modern JavaScript decision from ADR-0003. Maintain Node.js 22 as a CI-only verifier, and use `make webtest` to check the educational CPU functions and reproducible SVG.
3. Mark the shader and figure as `EXPLANATORY` and `PROPOSED_FOR_REVIEW`; no application-specific model or newly selected demonstrator is authorized.
4. Do not assign `MSR-MOD-0003`: procedural hashing, quantile teaching curves, and sampled glyphs are **illustrative algorithms**, not a reviewed mathematical or physical research model. A future use as a research model must first enter `mathematics/model_contracts/` under the model-contract schema with Python reference code and evidence.
5. Keep generated SVG source and `MANIFEST.sha256` synchronized. The original chapter content is not copied.

## Rejected alternatives

- Treating trigonometric fractional parts as a high-quality scientific random-number generator.
- Calling a smooth looking field statistically correlated with specified covariance without estimation.
- Randomizing a scientific diagram's topology/causal links or chart observations.
- Introducing Three.js, a front-end framework, or new package dependencies without need.
- Adding gold accents or colored backgrounds to the laboratory.

## Verification and promotion

Node.js tests check seed determinism, quantile monotonicity and endpoints, negative lattice indices, row resets, interpolation range/continuity, static SVG equivalence. GitHub CI plus SHA-256 manifest checks assess source reproducibility. Neither can certify WebGL2 rendering, accessibility across devices, psychological comprehension, empirical uncertainty, or physical validity.

**Before promotion:** independent review, GPU pixel-vs-CPU fixtures, browser/device matrix, color/contrast, keyboard access, reduced-motion behavior, and a valid figure provenance record. Revisit language policy before adding multiple production GPU apps.
