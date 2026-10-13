# Synthetic 2D Graph-to-Viability Demonstrator

Status: `EXPLORATORY COMPUTATIONAL DEMONSTRATOR / NOT THESIS EVIDENCE`

A small 2D viability example was constructed during the working session to verify the computational logic before introducing a physically calibrated P–W–T model.

# Reduced state

Let

$$
Y=(p,w),
$$

where:

- \(p\): normalized power-service state;
- \(w\): normalized water-service state.

Transportation enters through an accessibility factor \(a_T\) that scales usable repair/control capacity.

# Toy dynamics

$$
\dot p
=
r_P(1-p)
-c_{WP}(1-w)
-h_P
+u_P,
$$

$$
\dot w
=
r_W(1-w)
-c_{PW}(1-p)
-h_W
+u_W.
$$

These equations are synthetic and are not claimed to represent a calibrated physical P–W–T system.

# Admissible region

$$
K_{\rm sus}
=
\{(p,w):p\ge0.75,\;w\ge0.70,\;p\le1,\;w\le1\}.
$$

This is a simplified service/physical admissibility region, not a full sustainability set containing environmental, resource, and economic constraints.

# Controls

Controls satisfy

$$
u_P,u_W\ge0,
$$

with component limits and a shared budget. Transportation accessibility scales the usable control effort.

# Numerical method

- deterministic state integration: RK4;
- viability approximation: Saint-Pierre-style grid fixed-point iteration;
- grid size used in the exploratory run: \(61\times61\);
- time step: \(\Delta t=0.25\);
- discrete control grid used for one-step viability tests.

# Compared configurations

## Baseline

Stronger failure-amplifying power–water coupling and degraded transportation accessibility.

## Reinforced

Reduced cross-sector coupling severity and improved transportation-supported intervention accessibility.

# Exploratory numerical result

| Quantity | Baseline | Reinforced |
|---|---:|---:|
| Viable fraction of the chosen admissible grid | 0.238 | 0.928 |
| Fixed-point iterations | 61 | 36 |

Symmetric-difference fraction between the two grid viability masks:

$$
0.690.
$$

These numbers are **not thesis results**. They demonstrate only that the implemented computational chain can distinguish two synthetic parameterizations.

The grid fraction is not a coordinate-invariant resilience metric and must not be interpreted as a universal measure of resilience.

# Demonstrated conceptual distinction

The example makes visible the difference between

$$
Y\in K_{\rm sus}
$$

and

$$
Y\in\mathcal V_{\rm sus}.
$$

A point may be currently admissible while an uncontrolled trajectory leaves the admissible region. Under an admissible control policy, a state inside the viability kernel can remain viable.

# Next steps required for thesis-grade use

1. Replace the toy dynamics with a physically calibrated reduced P–W–T model.
2. Expand \(K_{\rm sus}\) beyond simple service thresholds to declared sustainability constraints.
3. Verify the reduced model against a higher-fidelity physical model.
4. Establish numerical convergence and error bounds.
5. Compute Euclidean boundary distance \(\rho_E\) as a baseline.
6. Introduce and calibrate \(g_\psi\).
7. Compute \(\rho_g\) and compare against \(\rho_E\).
8. Characterize smooth and nonsmooth boundary points.
9. Quantify set deformation under declared physical perturbations.
10. Propagate parameter/hazard uncertainty.
11. Compare geometry-guided interventions against conventional baselines under equal resources.

# Computational provenance note

The original working-session artifacts included an interactive HTML visualization, a PNG figure, and a CSV summary. They were generated in the conversation runtime and are not committed here because the GitHub connector used for this consolidation writes UTF-8 text files only. Reproducible code should be added in a subsequent implementation PR rather than encoding binary artifacts without provenance.

