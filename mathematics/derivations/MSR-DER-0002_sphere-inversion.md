# MSR-DER-0002 — Euclidean sphere inversion

- Model: `MSR-MOD-0002` (proposed mathematical verification fixture)
- Figure: `MSR-FIG-0002` (explanatory shader and static figure)
- Application, hazard, outcome and geography: **NOT_SELECTED**
- Source: Needham (1997), *Visual Complex Analysis*, Chapter 3, on inversion and Möbius geometry. The multivariate Jacobian below is derived directly from the displayed map.

## 1. Definition and units

Let `n ∈ {2,3}`, `c ∈ R^n`, `r > 0`, and `x ∈ R^n \ {c}`. All coordinates and `r` share one unit of length, or all are explicitly nondimensional. Define

```math
I_{c,r}(x) = c + \frac{r^2}{\|x-c\|_2^2}(x-c).
```

The domain and codomain are `R^n \ {c}`. Although the map extends to a compactified space by exchanging the center with infinity, **the numerical implementation does not represent infinity**.

## 2. Invariants and proof

Set `q=x-c`, `d=||q||>0`, and `s=r²/d²`. Then `I(x)-c = sq`. Therefore

```math
\|I(x)-c\|=\frac{r^2}{d}, \qquad
\|I(x)-c\|\,\|x-c\|=r^2.
```

Applying the map twice gives `I(I(x))-c = [r²/(r⁴/d²)] (r²/d²)q=q`, so

```math
I_{c,r}(I_{c,r}(x))=x.
```

If `d=r`, then `s=1`, so every point on the inversion sphere is fixed.

## 3. Jacobian and conformality

With unit radial vector `u=q/d`, differentiating `I(x)` yields

```math
J(x)=DI_{c,r}(x)=\frac{r^2}{d^2}(\mathbf I_n-2uu^\mathsf T).
```

The Householder matrix `H=I_n-2uu^T` satisfies `H^T H=I_n`. Hence

```math
J(x)^\mathsf T J(x)=\frac{r^4}{d^4}\mathbf I_n.
```

The derivative scales all tangent-vector lengths by `r²/d²` and preserves the **magnitude** of angles where defined; `det(H)=-1`, so inversion reverses orientation. It does **not** generally preserve distances, areas or physical states.

## 4. Visual encoding and sampling limits

On the left panel display a Cartesian grid as lines in a dimensionless source plane. In the right panel, a displayed location `y` is colored by sampling the original grid at `I(y)`, which is exactly the inverse map because `I∘I=id`. Source lines away from the inversion center map to circles passing through the center; source lines through it remain lines. The fixed sphere is shown as a circular outline. Antialiasing is based on finite screen-space derivatives; it is a **display approximation**, not part of the mathematical map.

**Render singularity:** a disk of radius `0.13` display units around the inversion center is explicitly masked. The mathematical domain excludes only the center; the larger rendered mask is a finite-precision and sampling safeguard. Shader execution uses device-dependent floating-point precision and must not be used to establish the mathematical invariants.

## 5. Verification / falsification

- `tests/unit/test_inversion.py`: known points, fixed sphere, 3D support, exact Jacobian, invalid input.
- `tests/properties/test_inversion_properties.py`: 240 seeded points across dimensions 2 and 3; round-trip, radial product, conformal metric identity, finite-difference derivative.
- Numerical reference: NumPy float64 with relative and absolute tolerance `2e-12` for representative well-separated points, and `3e-10` for finite-difference Jacobian.
- Renderer: WebGL2 fragment shader; visual appearance has not been independently browser-validated at authorship time.

## 6. Relevance and boundaries

This is **geometric literacy and a GPU verification exercise**. It does not define system dynamics, a viability kernel, recovery, infrastructure coupling, emissions or sustainability benefit. Its transferable lesson is that a coordinate transformation, simulation, and physical interpretation have different evidential requirements. Future resilience-specific graphics must encode model states from declared governing equations, without using arbitrary geometric distortions as if they represented physical mechanisms.
