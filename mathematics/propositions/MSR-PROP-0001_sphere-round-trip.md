# MSR-PROP-0001: Local exponential–logarithm round trip on $S^2$

- Model: `MSR-MOD-0001`
- Status: `ANALYTICALLY_ESTABLISHED_NUMERICALLY_TESTED`

## Proposition

For $p,q\in S^2$ with $q\neq -p$, let $v=\operatorname{Log}_p(q)$ be the principal logarithm. Then

$$
\operatorname{Exp}_p(v)=q.
$$

For $v\in T_pS^2$ with $\lVert v\rVert_2<\pi$, the corresponding principal inverse relation is

$$
\operatorname{Log}_p(\operatorname{Exp}_p(v))=v.
$$

## Proof status

The result follows by substitution into the closed-form sphere maps and by uniqueness of the principal minimizing geodesic away from the cut locus. This repository records the derivation in `MSR-DER-0001` and tests the computational form over deterministic generated inputs.

## Computational acceptance

For binary64 reference calculations, the maximum Euclidean residual in the registered experiment must satisfy

$$
\max_i\left\lVert\operatorname{Exp}_{p_i}
(\operatorname{Log}_{p_i}(q_i))-q_i\right\rVert_2\le 10^{-12}.
$$

Passing this condition verifies the reference implementation for the fixture. It is not an external validation of an application model.
