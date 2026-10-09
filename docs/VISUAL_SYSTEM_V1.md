# MSR-VIS-002 — Scientific Visual System v1

**Status:** `PROPOSED_FOR_REVIEW` · **Date:** 2026-10-09 · **Scope:** `NOT_SELECTED` · **Skill:** [scientific-visual-system](../skills/scientific-visual-system/SKILL.md)

## 1. Semantic separation

An **animation** encodes change under a declared rule; a **diagram** encodes a typed directed or undirected relation; a **mind map** encodes conceptual containment; a **chart** encodes numerical mapping on axes; a **mathematical figure** encodes a defined mathematical object under an explicit drawing projection. Do not classify a maturity ladder as a numerical chart unless meaningful quantities and scales exist. A validation ladder is generally a *stage diagram*, not data.

Every requested visual must declare: the question, object and status, coordinate or layout meaning, exact/approximate construction, source of claims/data, audience conclusion, provenance and known limits. Fail closed if a source model or edge inventory is missing.

## 2. Design tokens

Canvas, panels and boxes must be white (`#FFFFFF`). No gold, gradients, shadows, broad colored fills or speculative decorative forms. Use `#87CEFA` for supporting strokes, `#00BFFF` for primary geometry, `#17202A` labels, `#5D6D7E` secondary annotations, and `#C5D2DC` guides. Every mark has a declared role. The primary meaning must remain understandable without color. Headings ≥ 24 px, plot labels ≥ 15 px (larger for presentation), marks and line weights inspectable when scaled down. SVG is vector and remains sharp under zoom; dense labels and GPU output may not.

## 3. Type-specific checks

| Visual | Required model/semantic data | Failure-mode test | Nonclaim |
|---|---|---|---|
| Animation | analytic/numeric flow, initial value, time meaning, controls | round trip to start; end/limit; pause, seek, reset, reduced motion | not measured recovery |
| Diagram | node and directed-edge inventory, semantic edge labels | exactly the declared edge set | no implication of empirical causality |
| Mind map | parent map, acyclic taxonomy, stable hierarchy | unique node IDs, unique parent and root, no cycles | no causal link |
| Chart | equation/data, axes, units, range, origin and reference level | sample point values and monotonic/limit properties | no fake observations |
| Math figure | domain/codomain, projection, singularities and reference points | geometric incidence and stated limiting cases | 2D projected lengths need not be physical lengths |

## 4. First five-example contract

### 1 — Animation `MSR-FIG-0004` (model `MSR-MOD-0003`)
Equation: `dx/dτ=-x` for `x∈R²`, `τ≥0`. Closed form `x(τ)=e^{-τ}x₀`. Constraint `K={x:||x||₂≤1}`. A trajectory initially in `K` remains in `K`. Since no controls or disturbances are supplied, `Viab(K)=K` for this autonomous demonstration. For `||x₀||>1`, entering `K` later does not make it viable at `τ=0`. Example initial conditions A=(0.8,0.45) and B=(1.4,0.35). The time axis is dimensionless and contains **no** simulated physical recovery. Accessible time slider and playback; separate static first-frame SVG.

### 2 — Diagram `MSR-FIG-0005`
Exactly four directed stage transitions: theory → model → computation → visualization → interpretation. The arrows mean methodological handoffs, not validation inheritance. Annotation explicitly states that proof, uncertainty, and application validation have independent gates.

### 3 — Mind map `MSR-FIG-0006`
Root "Mathematics for Sustainability and Resilience"; three illustrative branches: Foundations (Geometry, PDEs, Dynamical systems); Methods (Optimization, Uncertainty, Computation); Interfaces (Viability, Networks, Visualization). This is a deliberately **nonexhaustive study taxonomy**, not a tested ontology or causal graph.

### 4 — Chart `MSR-FIG-0007` (model `MSR-MOD-0003`)
Analytical radius comparison for the *same fixture* as the animation. Plot `r_A(τ)=√(0.8²+0.45²)e^{-τ}` and `r_B(τ)=√(1.4²+0.35²)e^{-τ}`; dotted `r=1`. The outside-start curve crosses `r=1` at `τ=ln(√(1.4²+0.35²))` (a mathematical crossing, not physical recovery). Explicit `τ∈[0,3]`, `r∈[0,1.6]`, dimensionless axes and a source-data table of declared initial conditions.

### 5 — Figure `MSR-FIG-0008` (model `MSR-MOD-0004`)
Sphere `S²={p∈R³:||p||₂=1}`, pole `N=(0,0,1)`, plane `z=0`. For `P=(x,y,z)∈S²\{N}`, the stereographic projection is `Q=(x/(1-z),y/(1-z),0)`. The illustrated `P=(√3/2,0,-1/2)` projects to `Q=(1/√3,0,0)`. Plot using an explicitly documented orthographic 3D-to-2D camera; the screen drawing is *not a distance-preserving embedding*. The map is undefined at N.

## 5. Directory and identifiers

- `art/visual_suite/render.mjs`: deterministic generation source and CLI `--check`/`--write`.
- `art/visual_suite/registry.json`: source authority, genre, input assumptions, status and provenance for five IDs.
- `art/animations/viability_lab/model.mjs` and `index.html`: source code and browser access.
- `art/animations/viability_lab/static.svg`: exact static animation reference.
- `art/diagrams/model_to_visualization.svg`: typed stages.
- `art/mindmaps/mathematics_taxonomy.svg`: authored taxonomy.
- `art/charts/analytic_radius.svg`: reference curves.
- `art/mathematical_figures/stereographic_projection.svg`: sphere-plane map.
- `tests/regression/test_visual_suite.py` and Node.js unit/regression tests.

Identifiers are not recycled. A future real resilience model must be separately specified in `mathematics/model_contracts` with evidence and scientific governance, rather than silently upgrading these fixtures.

## 6. Reproducibility, CI and promotion

```sh
node art/visual_suite/render.mjs --check
node --test art/visual_suite/render.test.mjs art/animations/viability_lab/model.test.mjs
make verify-ci
python scripts/generate_manifest.py --check
```

The mathematical authorities are [MSR-MOD-0003](../mathematics/model_contracts/MSR-MOD-0003.json), [MSR-MOD-0004](../mathematics/model_contracts/MSR-MOD-0004.json) and [their derivations](../mathematics/derivations/MSR-DER-0003_linear-invariance-stereographic.md). The SVG files are byte-exact output of the generator. Do not edit output directly. Registry records source, parameter assumptions, semantic role, accessible descriptions and verification status. If the output changes, update both the generator and registry as necessary, then sync `MANIFEST.sha256`. Perform review of rendered labels, accessibility and actual browser animation before moving `PROPOSED_FOR_REVIEW` to an accepted gallery state. The mathematical evidence status and communication-evaluation status remain separate.
