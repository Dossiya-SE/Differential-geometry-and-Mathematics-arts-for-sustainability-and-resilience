# Seven bounded Chapter 10 code lessons

**Original educational examples** associated with `MSR-SKILL-SR-001`; conceptual attribution: Gonzalez Vivo and Lowe, [Chapter 10 — Random](https://thebookofshaders.com/10/). Equations and source here are newly authored. No material in the chapter is treated as an empirically verified stochastic model.

## L1 — Fractional sine: deterministic discontinuities

Concept: fractional-part operator `fract(x) = x - floor(x)`. Try `h(x)=fract(A sin(wx+phi))` for explicitly stated finite values and fixed coefficients. Learn floating-point periodicity, sensitivity, repeated inputs, and apparent disorder. In the source: `sineFragmentLesson`.

**Check:** same finite `x` returns identical output in `[0,1)` within representable arithmetic. Do not claim cryptographic strength, IID samples, uniformity, or spatial independence. GPU trig and precision are device dependent; large multipliers can destroy effective randomness.

## L2 — Bias transformation: controlled, mathematically identifiable distributions

Concept: `Y = U^gamma`, `gamma > 0`, for `U` genuinely uniform on `(0,1)`. Then `P(Y<=y) = y^(1/gamma)` and `E[Y]=1/(gamma+1)`; this is a conditional theorem under the stated input distribution, **not** a result about a sine hash. Source: `biasQuantile`.

**Check:** monotonicity, endpoints, gamma=1 identity; for a legitimately sampled uniform baseline, test estimated CDF or moments with finite-sample intervals. Use in a theoretical chart with a stated assumption; do not label it observed uncertainty.

## L3 — 2D hash: encode two integer cell coordinates

Concept: `H: Z² x Seed -> {0,...,2²⁴-1} / 2²⁴`, using 32-bit integer mixing and an explicit seed. Source: `hashCell`. The reference deliberately uses **24 output bits**, which can be represented exactly as float32 integers and is convenient for GPU comparison.

**Check:** deterministic identical inputs, finite in `[0,1)`, reproducible known fixtures including negatives and seed variations. This function is a procedural hash: collisions and correlations are possible. It is not a validated scientific pseudorandom-number generator.

## L4 — Cell coordinates: repeatable tiled geometry

Given a continuous coordinate `p` and frequency `s>0`, compute `i=floor(sp)` and local position `f=sp-i`. Stable `i` determines the cell value; `f in [0,1)` determines within-cell geometry. Source: `cellCoordinates`.

**Check:** negative inputs, cell constancy, local coordinate bounds, corner cases at grid lines. Spatial cell boundaries are rendering partitions, not necessarily geographical or infrastructure boundaries.

## L5 — Truchet-style orientation tiles

Select one of two diagonal glyphs using `H(i,j,seed)<0.5`. For an 8-by-8 image, draw only the diagonal strokes in a white-background SVG, providing explicit row/column labels. Source: `tileOrientation`; visual fallback: `art/shaders/randomness_lab/static.svg`.

**Check:** same seed and grid generate exactly identical paths; no topological connectivity or observed network semantics should be inferred from adjacent glyphs.

## L6 — Moving rows: parameterized *display* time

Define a row-indexed shift `d_j(t)=s_j t` with fixed, signed velocities `s_j`. Place a glyph using `floor(x-d_j(t))`. Source: `rowShift`.

**Check:** `d_j(0)=0`, linearity, sign, finite `t`, and repeatability on reset. Label `t` as display/animation time. This construction is **not a physical trajectory, restoration curve, or transport movement model**.

## L7 — Smooth, spatially dependent field: a deliberate extension

Build bilinearly interpolated *value noise* from neighboring integer-cell hashes using `q(t)=3t²-2t³`. This field is continuous, with a zero interpolant derivative at integer grid lines; it is not globally guaranteed to have any specified covariance function. Source: `smoothValueField`.

**Check:** exact corner values, continuity near adjacent cells, output range, and repeatability. Compute empirical correlograms/semivariograms only for declared realizations; never infer environmental correlation length or physical uncertainty without external evidence.

## Concrete example selection

| Requested task | Start with | Governing safeguard |
|---|---|---|
| Fragment-shader animation | L1, L6; extend with L7 | Freeze seed; display time is not system time |
| Structured diagram | L4 for layout only | Layout does not create scientific arrows |
| Research mind map | L4 for branch placement | Hierarchy is authored, not random |
| Chart showing distribution | L2 with analytic law | No pseudo-hash as observational dataset |
| Mathematical art figure | L3–L5 | Tile geometry has no physical interpretation |
| Spatial stochastic analysis | Neither hash nor tile suffices | Adopt evidence-supported physical/statistical covariance model |

## Why `dot()` is not itself a random-number generator

An arbitrary dot product `a·b` is not restricted to `[0,1]`; that bound holds only under additional normalization/alignment assumptions. Moreover a dot product and a sine hash do not establish a calibrated distribution. Use these operations solely as defined numerical transforms.

## Evaluation exercises

Explain the difference between deterministic repeatability and independent samples; derive L2's CDF; prove `0<=f_i<1` for L4 (finite real coordinates); identify why L5 cannot be used as a causal-network diagram; test L7 across negative cell boundaries; and design a small benchmark that compares GPU outputs to the 24-bit CPU hash at specified coordinates and precision.
