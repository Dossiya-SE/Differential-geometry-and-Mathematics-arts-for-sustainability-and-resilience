# Mathematical Visualization Learning Experiments

This directory implements `MSR-LA-001`, the repository's rigorous learning path for equation-driven mathematical art, geometry visualization, animation, and later scientific visualization.

## Governing rule

Every experiment must preserve the full chain

```text
mathematical definition
-> parameterization
-> implementation
-> testable invariants
-> rendered output
-> interpretation
-> limitations
```

A final image without the equation, code, tests, and experiment record is incomplete.

## Experiment families

| Range | Family | Required count |
|---|---|---:|
| MATART-001–015 | Cartesian scalar fields | 15 |
| MATART-016–030 | Radial/polar fields | 15 |
| MATART-031–045 | Interference fields | 15 |
| MATART-046–060 | Coordinate transforms | 15 |
| MATART-061–070 | Distance fields | 10 |
| MATART-071–080 | Masks/compositing | 10 |
| MATART-081–090 | Explicit RGB synthesis | 10 |
| MATART-091–100 | Time-dependent fields | 10 |

The numbering identifies the foundational 100-experiment sequence. Later differential-geometry and scientific-visualization experiments should receive separate registered identifiers rather than silently extending this sequence.

## Directory convention

```text
experiments/learning/
├── README.md
├── 01_equation_to_pixel/
│   ├── MATART_001.md
│   └── matart_001_radial_ring.py
└── studies/
    └── aurora_uvkq/
        ├── README.md
        └── render_uvkq.py
```

The `studies/` directory contains controlled analyses of supplied mathematical visuals. These are learning studies, not entries in the numbered 100-experiment sequence unless separately registered.

Future families should be added only when their mathematical objective is clear.

## Required experiment record

Each experiment record must state:

- ID
- objective
- classification (`mathematical-art`, `mathematical-visualization`, or `scientific-visualization`)
- domain
- governing equations
- parameters
- discretization/resolution
- numerical method
- expected invariants
- tests
- output path
- interpretation
- known limitations

## Validation principle

Tests should target mathematical or numerical properties rather than screenshots alone. Appropriate checks include:

- output shape;
- finite values;
- declared bounds;
- symmetry or invariance;
- known limiting cases;
- reproducibility for fixed parameters;
- analytic values at selected coordinates;
- numerical convergence where applicable.

Visual-regression tests may be added later, but they do not replace mathematical validation.

## First experiment

Run:

```bash
python -m pip install -e '.[dev,visualization]'
python experiments/learning/01_equation_to_pixel/matart_001_radial_ring.py
pytest tests/unit/test_visualization_fields.py -q
```

Before changing a parameter, write down the expected visual change. Compare the prediction with the render and record any mismatch.

## Controlled equation study: aurora UVKQ

The supplied aurora equation sheet is studied progressively through only the visible `U`, `V_nu`, `K_s`, and `Q_s` definitions. Run:

```bash
pytest tests/unit/test_aurora_uvkq.py -q
python experiments/learning/studies/aurora_uvkq/render_uvkq.py
```

The study explicitly separates equation transcription, analytic predictions, numerical safeguards near the rational singular line, diagnostic rendering, and scientific-boundary statements.
