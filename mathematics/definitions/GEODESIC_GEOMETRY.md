# Core differential-geometric definitions

## Riemannian manifold

A Riemannian manifold $(M,g)$ is a smooth manifold $M$ equipped with a smoothly varying positive-definite inner product $g_p$ on each tangent space $T_pM$.

## Geodesic

A geodesic is a curve $\gamma:I\rightarrow M$ whose covariant acceleration vanishes:

$$
\nabla_{\dot\gamma}\dot\gamma=0.
$$

This local definition does not by itself guarantee that a geodesic minimizes distance globally.

## Exponential map

For $v\in T_pM$ in its domain, the exponential map is

$$
\operatorname{Exp}_p(v)=\gamma_v(1),
$$

where $\gamma_v(0)=p$ and $\dot\gamma_v(0)=v$.

## Logarithm map

Where a unique selected minimizing geodesic exists, $\operatorname{Log}_p(q)$ is the tangent vector $v$ satisfying

$$
\operatorname{Exp}_p(v)=q.
$$

The logarithm is generally local and may be multivalued or undefined on the cut locus. Code must not present it as a globally invertible map.

## Evidence boundary

These are standard mathematical definitions supported by do Carmo (1992) and operationally represented in geometric-computation libraries such as Geomstats (Miolane et al., 2020). Their inclusion does not establish that a future sustainability or resilience state space is Riemannian.
