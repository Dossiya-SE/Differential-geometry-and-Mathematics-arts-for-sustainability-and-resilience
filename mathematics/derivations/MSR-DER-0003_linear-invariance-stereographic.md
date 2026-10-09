# MSR-DER-0003 — Two elementary mathematical references for Visual System v1

**Date:** 2026-10-09 · **Models:** `MSR-MOD-0003`, `MSR-MOD-0004` · **Figures:** `MSR-FIG-0004`, `MSR-FIG-0007`, `MSR-FIG-0008` · **Application:** `NOT_SELECTED`

## A. Autonomous flow and viability set

State space `R²`, dimensionless state `x=(x1,x2)`, dimensionless `τ>=0`, and autonomous ODE

```math
\dot{x}(\tau)=-x(\tau), \quad x(0)=x_0,\qquad
x(\tau)=e^{-\tau}x_0.
```

Proof: differentiating the proposed solution gives `d(e^{-τ}x0)/dτ=-e^{-τ}x0` and the correct initial state. For `V(x)=||x||²`,

```math
\frac{d}{d\tau}V(x(\tau))=2x^\top(-x)=-2\|x\|^2\le0.
```

Hence the closed unit disk `K={x:||x||<=1}` is forward invariant. Define the viability kernel with this **fixed autonomous system**, for all future `τ>=0`, and constraint `x(τ)∈K` for all `τ`. Every `x0∈K` satisfies that condition and no `x0∉K` satisfies it at `τ=0`. Therefore `Viab(K)=K` **for this system only**. A point outside with `r0>1` crosses the boundary at `τ*=ln(r0)`; this is **not** retroactive viability at `τ=0`.

The chart encodes `r(τ)=||x0|| exp(-τ)` exactly, sampled for finite SVG line approximation; its reference line `r=1` denotes the dimensionless constraint. Neither axis represents service reliability, emissions, restoration time, physical stress or intervention effects. Aubin (1991) supplies viability-theory context; all calculations here are elementary and derived as written.

## B. North-pole stereographic projection

Define `S²={(x,y,z):x²+y²+z²=1}`, north pole `N=(0,0,1)` and plane `z=0`. For `P=(x,y,z)∈S²\{N}`, the line `N+t(P-N)` intersects `z=0` at `t=1/(1-z)`, so

```math
\pi(P)=\left(\frac{x}{1-z},\frac{y}{1-z}\right).
```

For `Q=(u,v)`, put `s=u²+v²`. Its inverse on finite `R²` is

```math
\pi^{-1}(u,v)=\left(\frac{2u}{1+s},\frac{2v}{1+s},\frac{s-1}{1+s}\right).
```

Direct substitution proves the inverse lies on the unit sphere, excludes N for finite `u,v`, and composes to the identity on admissible input. For `P=(√3/2,0,-1/2)`, `Q=(1/√3,0)`. The SVG uses orthonormal projected view vectors `e1=(1,-1,0)/√2` and `e2=(-1,-1,2)/√6`, screen scale 175 and screen origin (455,410). The display is an **orthographic projection**, not a distance-preserving embedding of the sphere/plane. Its projected unit sphere silhouette is a circle of screen radius 175; N, P and Q remain collinear because orthographic projection is affine.

The map is mathematically undefined at N. Binary64 values in a declared `1e-14` denominator neighborhood are intentionally rejected as numerically underresolved; this finite guard is wider than the analytic singularity.

## C. Verification and evidential boundary

- Python tests: `tests/unit/test_visual_math.py`.
- Browser reference: `art/animations/viability_lab/model.mjs` with Node tests.
- Exact vector generator and audit: `art/visual_suite/render.mjs`, `render.test.mjs`.
- Literature: Aubin (1991), *Viability Theory*; Needham (1997), *Visual Complex Analysis*, for geometric motivation only.
- Mathematical-reference tests do not establish GPU device agreement, human comprehension, climate or infrastructure mechanisms, or an empirically validated viability kernel for any real system.
