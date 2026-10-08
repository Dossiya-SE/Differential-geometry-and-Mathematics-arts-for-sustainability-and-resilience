# JSON-driven tensor geometry

This directory is the machine-readable source for `MSR-FIG-0002`.

## Architecture

```text
tensor_geometry.json
        ↓
scripts/render_tensor_geometry.py
        ↓
figures/generated/MSR-FIG-0002_tensor-geometry.svg
        ↓
README / Quarto documentation
```

The JSON specification controls the selected system basis, hazard and mechanism coordinates,
synthetic coupling components, state-space metric samples, trajectories, viability geometry, and
decision annotation.

## Mathematical object

Let `V` denote the system-state space, `H` the hazard-coordinate space, and `M` the
mechanism-coordinate space. The demonstrator uses

```math
C\in V\otimes V^*\otimes H^*\otimes M^*,
\qquad
C^i{}_{jhm}=B^i{}_j a_h b_m.
```

For coordinates `η^h` and `μ^m`, contraction gives

```math
M^i{}_j=C^i{}_{jhm}\eta^h\mu^m,
\qquad
r^i=M^i{}_j x^j.
```

The renderer also evaluates local metric ellipsoids and a sampled metric distance from the current
state to the declared viability boundary.

## Evidence boundary

All coupling components in the default specification are `ILLUSTRATIVE_SYNTHETIC`. They are design
data for visualization and software verification, not empirical infrastructure estimates or an
identified constitutive law. Components are reported in one fixed basis; no empirical coordinate
transformation law is inferred from the demonstrator.

Run:

```bash
python scripts/render_tensor_geometry.py
python scripts/render_tensor_geometry.py --check
pytest -q tests/test_tensor_geometry.py
```

`--check` fails when the committed SVG or provenance record is stale relative to the JSON source.
