---
name: shader-randomness-scientific-visuals
description: Teach and apply procedural shader randomness to mathematically rigorous animations, diagrams, mind maps, charts, and figures without presenting visual noise as physical uncertainty. Use when a task involves GLSL, random fields, seeded design, tiles, generative mathematical art, or a proposed sustainability/resilience visualization.
---

# Scientific shader randomness — governed teaching skill

- Skill ID: `MSR-SKILL-SR-001`; version: `1.0.0`
- Research context: domain-neutral; application, hazard, system, outcomes and demonstrator remain `NOT_SELECTED`.
- Governing authority: [research architecture](../../docs/REPOSITORY_ARCHITECTURE.md), [visual standard](../../art/VISUAL_ENCODING_STANDARD.md), [research integrity](../../docs/RESEARCH_INTEGRITY.md), and [contribution rules](../../CONTRIBUTING.md).
- Teaching reference: Gonzalez Vivo and Lowe, [The Book of Shaders — Chapter 10: Random](https://thebookofshaders.com/10/). **Do not copy the book's example source, assets, or prose.** All linked implementation code here is independently written.
- Baseline: [seven code lessons](references/CHAPTER_10_LESSONS.md), [context-adaptation protocol](references/TASK_ADAPTATION.md), [deterministic JS reference](examples/random_fields.mjs), [tests](examples/random_fields.test.mjs), and [experimental WebGL laboratory](../../art/shaders/randomness_lab/README.md).

## When to apply

Trigger this skill for GLSL procedural geometry; a seeded shader, animated field, or tiled pattern; a scientific figure using random-looking placement; or a request to enhance repository animations, charts, diagrams, mind maps, or visuals based on Chapter 10. Prefer this skill only for stochastic-looking **rendering** or pedagogical study. If a task instead asks for empirical uncertainty, first use an evidence-supported statistical or physical model; this skill alone is insufficient.

## Mandatory workflow

1. **Classify** the requested artifact: `ANALYTICAL`, `EXPLANATORY`, `INTERPRETIVE`, or `PARTICIPATORY`; identify whether it is a chart, diagram, mind map, mathematical figure, or animation. Never automatically assign a research domain.
2. **Identify authority:** write the question, exact mathematical object, coordinate domain, units, scale, and epistemic status. Distinguish observations, model outputs, synthetic examples, and arbitrary design coordinates.
3. **Select a lesson** using [Chapter 10 lesson map](references/CHAPTER_10_LESSONS.md). Treat trigonometric hashes, integer hashes, discretized cells, decoratively moving rows, and correlated value noise as different constructions.
4. **Choose randomness semantics:** fixed seed and algorithm for a reproducible visual; sampled distribution only with a declared RNG and diagnostics; spatially correlated process only with a specified covariance/semivariogram and validation. A deterministic hash is **not** proof of IID draws, entropy, calibration, or physical causality.
5. **Derive before rendering:** specify map `f: domain -> codomain`, preconditions, endpoints and singularities, continuity/differentiability, and admissible parameter ranges; identify approximate versus exact results.
6. **Implement the CPU reference first**, using the source in `examples/random_fields.mjs` as a teaching fixture. Test known values, repeatability, bounds, negative coordinates, limiting behavior, invalid input, and fixed seeds before writing shaders.
7. **Implement the visual encoding**, then test shader/CPU agreement on shared fixtures and hardware limits. WebGL `highp` need not equal JS/NumPy float64. Require context-loss behavior, static fallbacks, keyboard operation and reduced-motion controls where relevant.
8. **Adapt to the task** using [task-specific contracts](references/TASK_ADAPTATION.md). Never use random placement to imply causal edges, observed data, risk probabilities, or validated infrastructure structure.
9. **Produce and audit** a code source, test log, fixed seed, artifact ID, figure provenance (encoding, known limitations, alt text), generation command, and bibliography/attribution as applicable. Update `MANIFEST.sha256` using `python scripts/generate_manifest.py --write` and run `make verify-ci`.
10. **Release gate:** report mathematical correctness, code verification, GPU/browser rendering, empirical validation, and communication impact as **separate statuses**. Keep a figure proposed until its own review gates pass.

## Required visual discipline

- Entire canvas and all panels white; no gold, gradients, filled cards, shadows, or decorative textures.
- Light Sky Blue `#87CEFA` for geometry accents; Deep Sky Blue `#00BFFF` for primary geometry; dark readable labels and neutral axis strokes.
- No arrow unless it encodes a verified dependency, sequence, flow, or explicit mathematical mapping; arrows must be clear and large. Random line orientations are **not** causal arrows.
- Axis units and scales must be explicit in charts; direct labels and line styles supplement color; maintain readable figures, static alternatives and reduced-motion access.
- Do not present an interpretive tile pattern as observed topology, rainfall, heat stress, spatial reliability, or resilience evidence.

## Acceptance checklist

- [ ] Mathematical question, object, domain, units and artifact class specified.
- [ ] Distinction between visual randomness and physical uncertainty documented.
- [ ] Algorithm, seed, tool versions and all parameters traceable.
- [ ] Properties, edge cases, numeric tolerances and negative examples tested.
- [ ] Display sources and fallback are reproducible with no hidden randomness.
- [ ] Figures have captions, provenance and accessible text alternatives.
- [ ] No new application domain or invalid cross-sector claim introduced.
- [ ] Integrity manifest and applicable CI checks pass; unresolved GPU review disclosed.

## Removal and escalation

Stop if randomness is used as a substitute for measured mechanisms, if a chart fabricates measurements, or if a mind map's layout is confused with evidence of causation. For a new physical model, obtain a reviewed model contract, independent data, uncertainty specification, and research-scope decision first. For more than one production interactive browser artifact, follow the architecture's TypeScript/pinned-dependency decision gate rather than expanding unchecked JavaScript infrastructure.
