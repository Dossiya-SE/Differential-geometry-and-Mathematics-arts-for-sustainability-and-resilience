# MSR-DER-0001: Exponential and logarithm maps on the unit two-sphere

- Model: `MSR-MOD-0001`
- Version: `1.0.0`
- Status: `REFERENCE_DERIVATION`

Let

$$
S^2=\{x\in\mathbb{R}^3:x^\top x=1\},\qquad
T_pS^2=\{v\in\mathbb{R}^3:p^\top v=0\}.
$$

For $v\in T_pS^2$ and $r=\lVert v\rVert_2$, the unit-sphere exponential is

$$
\operatorname{Exp}_p(v)=
\begin{cases}
p, & r=0,\\
\cos(r)p+\dfrac{\sin(r)}{r}v, & r>0.
\end{cases}
$$

The output remains on $S^2$ because $p^\top v=0$:

$$
\lVert\operatorname{Exp}_p(v)\rVert_2^2
=\cos^2(r)\lVert p\rVert_2^2
+\sin^2(r)\dfrac{\lVert v\rVert_2^2}{r^2}=1.
$$

For $p,q\in S^2$, define a numerically stable principal angle

$$
c=\operatorname{clip}(p^\top q,-1,1),\qquad
s=\lVert q-cp\rVert_2,\qquad
\theta=\operatorname{atan2}(s,c).
$$

When $0<\theta<\pi$, the principal logarithm is

$$
\operatorname{Log}_p(q)=
\frac{\theta}{s}(q-cp).
$$

At $q=p$, it is the zero tangent vector. At $q=-p$, the minimizing direction is non-unique; the reference implementation raises `AntipodalError` rather than selecting an undocumented direction.

Numerical code clips the inner product, uses `atan2(s,c)` instead of `arccos(c)` for better conditioning near angles zero and $\pi$, applies explicit coincident and antipodal branches, verifies tangency, and renormalizes the exponential output only to control floating-point drift.
