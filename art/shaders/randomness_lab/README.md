# MSR-FIG-0003 — Chapter 10 mathematical randomness laboratory

**Artifact class:** `EXPLANATORY`. **Status:** `PROPOSED_FOR_REVIEW`. **Scientific application:** `NOT_SELECTED`. **Physical/empirical validation:** `NOT_VALIDATED`; communication impact `NOT_EVALUATED`.

The seven-mode experimental [browser application](index.html) demonstrates original mathematical techniques associated with concepts from Gonzalez Vivo and Lowe, [The Book of Shaders, Chapter 10 — Random](https://thebookofshaders.com/10/). None of its code or artwork is copied from that chapter. The derivative source is governed by [MSR-SKILL-SR-001](../../../skills/shader-randomness-scientific-visuals/SKILL.md).

## How to run

Serve the repository root, not this subdirectory:

```sh
python -m http.server 8000
```

Then visit `http://localhost:8000/art/shaders/randomness_lab/`. WebGL2 is required for interactivity, but the `static.svg` two-orientation tile example is available as a standalone vector figure and GPU-failure fallback. No external JavaScript or network dependency is used.

## Map: exercise -> independent code -> meaning

| Mode | Source function | Geometry | Limits |
|---|---|---|---|
| L1 Fractional sine | `sineFragmentLesson` | plotting a discontinuous scalar function | no statistical randomness guarantee; aliasing |
| L2 Power law | `biasQuantile` | `y=u^gamma` and `y=u` comparison | theoretical CDF only for uniform input |
| L3 2D hash | `hashCell` | cell dots of varying size | 24 output bits; collisions possible |
| L4 Lattice cells | `cellCoordinates` | indexed coordinate cells | not a geographical grid |
| L5 Orientation tiles | `tileOrientation` | two diagonal glyphs per square | glyph adjacency is not empirical topology |
| L6 Moving rows | `rowShift` | row-specific time-dependent shifts | display time is not physical time |
| L7 Smooth value field | `smoothValueField` | contour drawing over interpolated hashes | no calibrated covariance or physical field |

The JS reference functions and their deterministic tests are under `skills/shader-randomness-scientific-visuals/examples/`. GLSL has analogous shader calculations but is **not validated numerically against GPU pixel outputs**; actual browser/hardware validation is required before gallery approval.

## Reproducibility

```sh
make webtest
node skills/shader-randomness-scientific-visuals/examples/render_static.mjs --check
python scripts/generate_manifest.py --check
```

The fixed demonstration seed is `20261009`. The SVG is reconstructed directly from the seeded integer hash; output of `render_static.mjs` must match the committed `static.svg` byte-for-byte. Changing any input seed is a **new generated artifact**, not evidence of changing hazard conditions.

## Visual semantics and accessibility

- White canvas and panels; `#87CEFA` secondary geometry; `#00BFFF` primary geometrical marks; dark legible text.
- No gradients, fills or shadows. Tiles and hash dots encode **only synthetic mathematical values**, not data, risk, causal arrows, or infrastructure edges.
- Large labels, equations, transparent source and clear text alternative. Control values and selected lesson remain keyboard accessible; a reduced-motion preference disables animation.
- When GPU initialization fails or the context is lost, controls are disabled and the fixed static tile figure is shown. Mode-specific animation or alternate renderings are not implied by the static figure.
- GPU precision, float32 trigonometry, sampling, integer mixing, pixel antialiasing, contrast and resizing need device-level review. Do not claim full renderer validation from the Node.js tests.

## Publication boundary

The exact geometric source is versioned with `MSR-FIG-0003` [provenance](provenance.json). It is a **teaching illustration**, not a sustainable-resilience simulation. Adopt a reviewed physical/statistical model, units, evidence, correlation and external validation **before** using similar maps to represent a physical quantity. No new geographic, system, hazard, sustainability or resilience scope is selected.
