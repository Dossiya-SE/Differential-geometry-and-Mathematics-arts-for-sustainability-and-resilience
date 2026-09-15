# MVS Architecture Foundation v1

This foundation freezes the first production contracts behind Mathematical Visual Design Studio Pro.

## Governing separation

```text
semantic mathematics/data/topology
        ↓
Semantic Visual IR v1
        ↓
Presentation IR v1
        ↓
backend-specific lowering
        ├─ SVG / D3 / Vega-Lite
        ├─ Three.js WebGPU/WebGL2
        ├─ VTK / PyVista
        ├─ Tectonic / Asymptote
        ├─ Manim
        └─ Blender
```

The semantic project is the authority. Renderer objects are derivatives.

## Frozen contracts

- `schemas/visual-ir-v1.schema.json`
- `schemas/presentation-ir-v1.schema.json`
- `schemas/engine-pack-v1.schema.json`
- `schemas/render-record-v1.schema.json`
- `src/ir/v1.ts`

The contract covers mathematical expressions, units/domains, parametric surfaces, typed computational graphs, scientific charts, presentation references, renderer policy, epistemic status, fail-closed validation, engine identity and immutable render provenance.

## Reference implementations used by the conformance suite

- Ajv 8.20.0 — JSON Schema 2020-12 validation.
- ELK.js 0.12.0 — layered/orthogonal graph layout. ELK remains a layout service, not the semantic graph model.
- Vega-Lite 6.4.3 — declarative scientific-chart lowering.
- React Flow 12.11.3 — pinned interaction dependency for the upcoming typed node workspace. It does not define mathematical semantics.

## Non-compensatory QA

The architecture intentionally separates:

`SCHEMA`, `MATH`, `DIMENSION`, `NUMERICAL`, `TOPOLOGY`, `DATA`, `VISUAL_ENCODING`, `RENDER`, `PROVENANCE`, and `REPRODUCTION`.

A successful render must never erase a mathematical, dimensional, provenance or reproducibility failure.

## Golden path

The first conformance project encodes a torus, its Gaussian-curvature dependency graph, a curvature scientific chart, presentation mappings, exact units, numerical policy and an illustrative epistemic status. Tests verify:

1. schema conformance;
2. deterministic canonical serialization;
3. fail-closed graph typing/units;
4. ELK layout execution;
5. Vega-Lite compilation;
6. engine-pack least privilege;
7. immutable render-record structure.

## Deliberate boundaries

This milestone does **not** claim that React Flow, VTK, JAX, Manim, Blender, Julia/Makie, Graphviz or collaboration are fully integrated. It establishes contracts they must satisfy before deeper integration.
