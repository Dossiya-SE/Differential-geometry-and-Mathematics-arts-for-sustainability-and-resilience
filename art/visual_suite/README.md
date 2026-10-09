# Scientific Visual System v1 — five reproducible visual families

**Current status:** `PROPOSED_FOR_REVIEW`. **Application decision:** `NOT_SELECTED`.

This is a *domain-neutral mathematical and semantic reference set*, not an empirical sustainability or resilience study. Learn the distinction among five visual families via the [governing SKILL.md](../../skills/scientific-visual-system/SKILL.md) and the [formal visual standard](../../docs/VISUAL_SYSTEM_V1.md).

| Step | Genre | Open source figure | What it communicates |
|---|---|---|---|
| 1 | Animation | [Interactive viability lab](../animations/viability_lab/index.html) / [static](../animations/viability_lab/static.svg) | dimensionless invariance under x′ = −x |
| 2 | Diagram | [Model-to-interpretation pipeline](../diagrams/model_to_visualization.svg) | typed methodological sequence |
| 3 | Mind map | [Mathematics taxonomy](../mindmaps/mathematics_taxonomy.svg) | conceptual hierarchy, not causal edges |
| 4 | Chart | [Analytic radial curves](../charts/analytic_radius.svg) | quantitative, *not observed*, functions of time |
| 5 | Mathematical figure | [Stereographic projection](../mathematical_figures/stereographic_projection.svg) | mathematical point correspondence |

The [machine-readable registry](registry.json) states the exact figure IDs, authorities, scope, validity statuses and asset paths. [render.mjs](render.mjs) is the sole generator for the five SVGs; the SVGs are stored for preview, accessibility and standalone reproducibility.

### Verification

```sh
node art/visual_suite/render.mjs --check
node --test art/visual_suite/render.test.mjs art/animations/viability_lab/model.test.mjs
make verify-ci
python scripts/generate_manifest.py --check
```

For the interactive animation, serve the repository root using `python -m http.server 8000` and open `http://localhost:8000/art/animations/viability_lab/`. The static SVG communicates the initial frame if scripts are unavailable. Canvas/panels are white; all accents have meaning and the coordinate figures are vector graphics.

**Limit:** Tests establish only bounded internal mathematical/semantic and source-reproduction properties. Browser rendering, typographic evaluation, scientific interpretation and communication effects remain separately unvalidated.
