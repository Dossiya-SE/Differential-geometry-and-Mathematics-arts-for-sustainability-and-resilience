---
name: scientific-visual-system
description: Design and verify domain-neutral scientific animations, diagrams, mind maps, quantitative charts, and mathematical figures using explicit contracts, deterministic SVG generation, accessible representations, and evidence boundaries.
---

# Scientific Visual System v1 — governed artifact skill

Authority: [MSR-VIS-001](../../art/VISUAL_ENCODING_STANDARD.md), [v1 standard](../../docs/VISUAL_SYSTEM_V1.md), [registry](../../art/visual_suite/registry.json), repository architecture and research-integrity policy.

## Activation and classification

Apply this skill to requests to make or revise an animation, scientific diagram, concept mind map, quantitative chart, mathematical figure, or their mathematical-art representations. **Do not apply one type's semantics to another.** Select one family before generating any image or code:

| Family | Shows | Does not independently show |
|---|---|---|
| Animation | a specified time flow or parameter transformation | a validated physical trajectory |
| Diagram | typed direction, physical link, model pipeline, or evidence relationship | a quantitative result or a causal fact without evidence |
| Mind map | concepts and parent–child grouping | causal interactions, functional dependence or statistical correlation |
| Chart | numeric functions, observations or theoretical comparisons with axes | validation from visually attractive curves |
| Mathematical figure | a defined set, surface, map, projection or geometric object | an empirically validated physical outcome |

## Required ten-step procedure

1. **Scope** — identify the audience, one-sentence message, use case, target visual class, and scientific question.
2. **Authority** — locate exact source, proposition, model contract or declared *illustrative mathematical model*. Do not invent data, units, causal edges or domain selection. Preserve `NOT_SELECTED` unless the actual application-selection protocol authorizes a change.
3. **Mathematics or semantics** — explicitly write domain, codomain, state/time/scale, governing equations, edge types or parent–child relations. State whether the example is analytical, explanatory or interpretive.
4. **Coordinates** — declare the rendering map (world-to-screen, projection, axis mapping) and admissible inputs. Avoid implying a 2D projection preserves lengths or angles without proof.
5. **Reference first** — compute state or quantitative values independently of rendering. For a chart verify coordinates against `f(x)`; for a diagram check edges against the authored edge list; for mind maps check each parent; for animation check the governing flow; for figures check incidence, singularities and limits.
6. **Generate deterministically** — use the source `art/visual_suite/render.mjs` to create five SVGs. Never hand-modify a generated SVG without editing its generator; run `node art/visual_suite/render.mjs --check` after generating.
7. **Encode honestly** — white canvas and box interiors, Light Sky Blue `#87CEFA` supporting geometry, Deep Sky Blue `#00BFFF` primary geometry, dark type, neutral secondary strokes, no gold/gradients/shadows/filled panels. Large arrows only for directed, declared relationships. In charts use axis labels, units, tick marks and direct curve labels.
8. **Accessibility** — provide SVG `title`/`desc`, labels and keyboard support; animations need pause/reset/seek and reduced motion; charts need data/equation equivalents; mind maps need textual concept inventory.
9. **Provenance** — assign a unique `MSR-FIG-NNNN` ID, status, exact source/generation command, parameter and unit values, figure class, alt text and explicit validity/communication states in the registry. Separate mathematical verification from browser rendering, empirical validation and communication evaluation.
10. **Test/review** — run Node analytic tests plus byte-exact SVG generator tests, Python structural tests, `make verify-ci`, SHA-256 manifest generation/check, GitHub workflows and independent browser review before scientific gallery promotion. Report failure, scope restrictions and unresolved checks. Do not equate a passed CI with empirical validity.

## Step-by-step reference artifacts

1. **Animation:** `art/animations/viability_lab/`, `MSR-FIG-0004`. State `x'(t)=-x(t)`; unit disk `K`. Demonstrate invariance of points starting in `K` and distinguish outside-start states from viable ones. Closed-form analytic flow; dimensionless time only.
2. **Diagram:** `art/diagrams/model_to_visualization.svg`, `MSR-FIG-0005`. Five semantic stages and four typed directional arrows. No evidence upgrades are implied.
3. **Mind map:** `art/mindmaps/mathematics_taxonomy.svg`, `MSR-FIG-0006`. Root, three branches and nine leaves; connectors mean taxonomy only.
4. **Chart:** `art/charts/analytic_radius.svg`, `MSR-FIG-0007`. Analytic radii `r_i(t)=r_i(0)e^{-t}`, dimensionless time and radial threshold `1`. No observational data or unearned viability claims.
5. **Mathematical figure:** `art/mathematical_figures/stereographic_projection.svg`, `MSR-FIG-0008`. Projection from north pole of `S²` to equatorial plane; point correspondence and singular pole clearly declared. Orthographic view is illustration, not metric preservation.

## Task adaptation

Read [v1 standard](../../docs/VISUAL_SYSTEM_V1.md) and the registry first. Adapt type, data and message to the actual task; **do not introduce stochastic textures** into formal math unless randomness is the object being studied. The Chapter-10 [procedural shader skill](../shader-randomness-scientific-visuals/SKILL.md) is only an optional subordinate rendering lesson, never a substitute for equations, typed edges, observed data or valid inference. Domain-focused Power–Transportation diagrams require their own supported interface inventory, nonselected domain status review, and separate evidence.

## Acceptance boundary

The v1 suite contains original *explanatory mathematical fixtures*. It is not an approved research demonstrator. A schema/CI pass establishes source reproducibility and bounded internal checks, not GPU, human-comprehension, physical validation or resilience/sustainability impacts. Never use these example curves as measured service, exposure, or recovery time series.
