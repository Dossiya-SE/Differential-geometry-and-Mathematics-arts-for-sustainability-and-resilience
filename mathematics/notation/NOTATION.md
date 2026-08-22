# Notation registry

- Registry ID: `MSR-NOT-001`
- Version: `1.0.0`

| Symbol | Domain | Meaning | Unit | Scope |
|---|---|---|---|---|
| $M$ | smooth manifold | Generic state space | context-dependent | Project-wide |
| $T_pM$ | vector space | Tangent space at $p\in M$ | inherited | Differential geometry |
| $g_p$ | bilinear form on $T_pM$ | Riemannian metric at $p$ | context-dependent | Differential geometry |
| $d_g(p,q)$ | $\mathbb{R}_{\ge 0}$ | Geodesic distance under $g$ | context-dependent | Differential geometry |
| $\operatorname{Exp}_p$ | $T_pM\rightarrow M$ locally | Riemannian exponential map | inherited | Differential geometry |
| $\operatorname{Log}_p$ | $M\rightarrow T_pM$ locally | Principal Riemannian logarithm | inherited | Differential geometry |
| $S^2$ | subset of $\mathbb{R}^3$ | Unit two-sphere | dimensionless | `MSR-MOD-0001` |
| $p,q$ | $S^2$ | Sphere points | dimensionless | `MSR-MOD-0001` |
| $v$ | $T_pS^2$ | Tangent vector at $p$ | radians under unit radius | `MSR-MOD-0001` |
| $\varepsilon_{abs}$ | $\mathbb{R}_{>0}$ | Absolute numerical tolerance | output unit | Numerical tests |
| $\varepsilon_{rel}$ | $\mathbb{R}_{>0}$ | Relative numerical tolerance | dimensionless | Numerical tests |

## Collision rule

Notation defined by a focal source is preserved in its case-study folder. Project-wide notation is not retroactively imposed on quoted source notation. Every reuse must state which scope controls the symbol.
