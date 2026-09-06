# Manim candidate renderer layer

This directory contains **renderer-independent animation specifications and candidate
Manim integration policy** for `MSR-VM-001`.

It intentionally contains no production Manim scene yet.

## Governing rule

> A scene is a renderer implementation of an animation specification. It is not the
> mathematical source of truth.

## Contents

| Path | Purpose |
|---|---|
| `catalog.yaml` | Forty-concept visual-mathematics roadmap |
| `specs/` | Six flagship `MSR-ANIM-xxxx` specifications |
| `../../schemas/animation-spec.schema.json` | Machine-readable animation contract |
| `../../scripts/validate_animation_specs.py` | Standalone specification validator |
| `../../tests/regression/test_animation_specs.py` | CI regression gates |

## Candidate renderer status

`MANIM_CE = ADMITTED_FOR_SPECIFICATION_PROTOTYPING`

This means:

- specifications may explicitly target Manim CE as the first implementation candidate;
- no Manim package is imported by the scientific core;
- no scene is `VALIDATED` merely because it renders;
- runtime dependencies are deferred until the first reference-scene PR.

## Semantic source

All visual semantics must resolve through `../design_tokens.json` (`MSR-VIS-001`).
In particular:

- chain colors encode declared conceptual chains;
- evidence state uses line style/width as well as color;
- color is never the sole encoding;
- alt text is mandatory;
- static fallback is mandatory;
- reduced-motion support is mandatory.

## Scene contract

Before code exists, each scene specification must declare:

1. scientific question;
2. mathematical object and state space;
3. equations;
4. assumptions;
5. sustainability/resilience interpretation and its boundary;
6. semantic visual encodings;
7. motion semantics;
8. mathematical invariants;
9. validation tests;
10. accessibility;
11. provenance.

## Renderer implementation rules

Future Manim scene code must:

- read or compile from the corresponding spec;
- use stable object IDs;
- separate geometry/state from style;
- avoid hidden mutation of mathematical state;
- pin stochastic seeds;
- expose render configuration;
- emit provenance;
- produce a static fallback;
- avoid decorative motion that has no declared semantic role.

## Render profiles planned for the reference scene

| Profile | Purpose | Status |
|---|---|---|
| `draft-cairo` | Fast local review | planned |
| `ci-cairo` | Deterministic CI fixture | planned |
| `publication-cairo` | High-quality release artifact | planned |
| `opengl-experimental` | GPU-specific research only | blocked until justified |

## Promotion rule

A scene moves

```text
SPECIFIED -> PROTOTYPE -> VALIDATED
```

only through explicit pull requests carrying the required test and provenance evidence.
