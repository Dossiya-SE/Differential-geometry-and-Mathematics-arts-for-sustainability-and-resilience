# Thesis 1 — Graph-to-Viability Geometry of Sustainable and Resilient P–W–T Systems

Status: `PROPOSED / CANDIDATE GAP STRUCTURE`

## Scientific identity

$$
\boxed{
\mathfrak G_{\rm PWT}
\rightarrow
F_{\mathfrak G}
\rightarrow
K_{\rm sus}
\rightarrow
\mathcal V_{\rm sus}
\rightarrow
(\mathcal M_{\mathfrak G},g_\psi),\rho_g
\rightarrow
S^{\mathcal V}
\rightarrow
e^\star
\rightarrow
\{\mathfrak G^\star,u^\star\}
}
$$

The thesis asks how infrastructure architecture and dynamic interfaces shape the set of sustainable futures available to a coupled Power–Water–Transportation system.

## System representation

Let

$$
\mathfrak G
=
\{G_P,G_W,G_T,E_{PW},E_{PT},E_{WT}\},
$$

with each sector graph

$$
G_i=(V_i,E_i).
$$

Dynamic interfaces are represented as

$$
I_{ij}=(e_{ij},z_{ij},\theta_{ij},G_{ij}),
$$

where the interface state evolves according to

$$
\dot z_{ij}=G_{ij}(x_i,x_j,z_{ij},u,\eta;\theta_{ij}).
$$

The coupled state is

$$
X=[x_P,x_W,x_T],\qquad
Z=[z_{PW},z_{PT},z_{WT}],\qquad
Y=(X,Z).
$$

## Graph-to-dynamics foundation

Define an admissible graph space

$$
\mathscr G_{\rm PWT}
=
\{\mathfrak G:\text{physical, capacity, connectivity and engineering constraints hold}\}.
$$

The graph-conditioned dynamics are

$$
\mathcal F:
\mathscr G_{\rm PWT}\times\Theta
\rightarrow
\mathfrak X,
\qquad
(\mathfrak G,\theta)\mapsto F_{\mathfrak G},
$$

with

$$
\dot Y=F_{\mathfrak G}(Y,u,\eta;\theta).
$$

This map is a **foundation**, not by itself a novelty claim.

## Sustainable admissibility

Use a non-compensatory admissible set

$$
K_{\rm sus}(t)
=
K_{\rm phys}
\cap K_{\rm serv}
\cap K_{\rm env}
\cap K_{\rm resource}
\cap K_{\rm econ}.
$$

Where appropriate evidence exists, a social/equity constraint may be added, but should not be quantified without data.

The distinction is essential:

$$
Y\in K_{\rm sus}
\quad\Rightarrow\quad
\text{acceptable now},
$$

while

$$
Y\in\mathcal V_{\rm sus}
\quad\Rightarrow\quad
\text{feasible controls exist to maintain acceptable operation}.
$$

## Sustainable viability

$$
\mathcal V_{\rm sus}(t;\mathfrak G)
=
\operatorname{Viab}_{F_{\mathfrak G,t}}[K_{\rm sus}(t)].
$$

## Signature graph-to-viability map

$$
\boxed{
\Psi:
(\mathscr G_{\rm PWT},d_{\mathscr G})
\rightarrow
(\mathscr V,D_{\mathcal V}),
\qquad
\Psi(\mathfrak G)=\mathcal V_{\rm sus}(\mathfrak G)
}
$$

The main structural question is the stability and sensitivity of

$$
\mathfrak G\mapsto\mathcal V_{\rm sus}(\mathfrak G).
$$

For finite structural perturbations,

$$
S_{\mathfrak G}^{\mathcal V}
=
\frac{
D_{\mathcal V}[\Psi(\mathfrak G_2),\Psi(\mathfrak G_1)]
}{
d_{\mathscr G}(\mathfrak G_1,\mathfrak G_2)
}.
$$

For an interface parameter,

$$
S_e^{\mathcal V}(\delta)
=
\frac{
D_{\mathcal V}[\mathcal V(\theta+\delta e),\mathcal V(\theta)]
}{|\delta|}.
$$

Finite perturbations are preferred before derivative-based sensitivity because differentiability of the set-valued map must not be assumed.

## Geometry layer

Use a continuous state representation

$$
Y\in(\mathcal M_{\mathfrak G},g_\psi).
$$

A candidate physically calibrated metric is

$$
g_\psi(Y)
=
J_{\tilde h}(Y)^\top W_\psi J_{\tilde h}(Y)+\lambda I,
$$

where \(\tilde h\) contains normalized physically and service-relevant consequences. The metric requires SPD verification, calibration, unit/normalization analysis, and comparison with \(g_E=I\).

Define the intrinsic viability margin

$$
\rho_g(Y,t)
=
d_{g_\psi}(Y,\partial\mathcal V_{\rm sus}).
$$

At smooth points, differential geometry may be used. At nonsmooth intersections of active constraints, use tangent and normal cones:

$$
T_{\mathcal V}(Y),\qquad N_{\mathcal V}(Y).
$$

## Uncertainty-aware criticality

Propagate uncertainty through

$$
\xi
\rightarrow
\mathcal V
\rightarrow
\rho_g
\rightarrow
S^{\mathcal V}
\rightarrow
e^\star.
$$

Report quantities such as

$$
P(e^\star=e)
$$

and pairwise ranking confidence, e.g.

$$
P(S_{PW}^{\mathcal V}>S_{PT}^{\mathcal V}).
$$

## Engineering interventions

Structural mitigation:

$$
(\mathfrak G^0,\theta^0)
\rightarrow
(\mathfrak G^\star,\theta^\star).
$$

Operational adaptation:

$$
u(t)\rightarrow u^\star(t).
$$

Multi-timescale interpretation:

$$
\begin{array}{rcl}
\text{seconds--hours}&\rightarrow&u(t),\\
\text{months--years}&\rightarrow&\theta,\\
\text{years--decades}&\rightarrow&\mathfrak G.
\end{array}
$$

Equal-budget validation:

$$
B_{\mathcal V}=B_{\rm conventional}=B,
\qquad
\eta=\frac{\Delta R_{\rm sus}}{B}.
$$

## Thesis identity in one sentence

> Architecture determines dynamics; dynamics determine sustainable viable futures; geometry characterizes those futures; perturbations reveal what threatens them; interventions test whether that knowledge improves resilience.

