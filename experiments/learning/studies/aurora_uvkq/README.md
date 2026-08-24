# Aurora UVKQ Equation Study

## Purpose

This is a controlled educational reconstruction of only four equations visible in the supplied aurora equation sheet:

\[
U(x,y)=\left(y+\frac{1001}{10000}\right)^{-1}\left(x+\frac14\right),
\]

\[
V_\nu(x,y)=\left(y+\frac{1001}{10000}\right)^{-1}\left(1-\frac{x}{4}\right)+\frac{\nu}{100},
\]

\[
K_s(y)=\left(\frac{50}{49}\right)^s\left(y+\frac{1001}{10000}\right)^{-1},
\]

and

\[
\begin{aligned}
Q_s(x,y)={}&3\left(x+\frac{s}{500}\right)K_s(y)+2\cos K_s(y)\\
&+\frac25\cos\left(5\left(x+\frac{s}{500}\right)K_s(y)+8K_s(y)\right)\\
&+\frac1{10}\cos\left(15\left(x+\frac{s}{500}\right)K_s(y)-18K_s(y)\right).
\end{aligned}
\]

The study does **not** reproduce the complete artwork and is **not** a physical aurora simulation. Its purpose is to learn how perspective-like denominators, geometric scale families, and multi-frequency oscillations generate procedural structure.

## 1. Domain inherited from the pixel normalization

For a `2000 x 1200` image, the visible sheet maps pixel indices to

\[
x=\frac{m-1000}{600},\qquad y=\frac{601-n}{600}.
\]

Therefore the sampled domain is approximately

\[
x\in[-1.665,1.667],\qquad y\in[-0.998,1].
\]

All four study equations contain the denominator

\[
y+0.1001.
\]

Hence there is a mathematical singular line at

\[
y=-0.1001.
\]

The renderer deliberately leaves a small diagnostic guard band around this line. This is a visualization safeguard only; it does not alter the analytic definition.

## 2. Step A — Understand U

\[
U(x,y)=\frac{x+0.25}{y+0.1001}.
\]

At fixed `y`, `U` is linear in `x`.

At fixed `x`, the denominator causes strong magnification as `y` approaches `-0.1001`.

Before rendering, predict:

- `U=0` along `x=-0.25`, away from the singular line;
- `|U|` grows without bound as `y -> -0.1001` unless `x=-0.25`;
- the sign of `U` changes when either the numerator or denominator changes sign.

This is the first perspective-like coordinate transform to inspect.

## 3. Step B — Understand V_nu

\[
V_\nu(x,y)=\frac{1-x/4}{y+0.1001}+\frac{\nu}{100}.
\]

The three values `nu=0,1,2` differ only by exact offsets:

\[
V_1-V_0=0.01,\qquad V_2-V_0=0.02.
\]

This makes the channel index mathematically testable rather than visually guessed.

## 4. Step C — Understand K_s

\[
K_s(y)=\left(\frac{50}{49}\right)^s\frac{1}{y+0.1001}.
\]

For any fixed safe `y`, consecutive scales satisfy

\[
\frac{K_{s+1}(y)}{K_s(y)}=\frac{50}{49}.
\]

Thus the fifty members form a geometric scale family. Increasing `s` does not change the singular line; it multiplies the field by a controlled scale factor.

## 5. Step D — Decompose Q_s before rendering

Write

\[
Q_s=L_s+O_s,
\]

where

\[
L_s=3\left(x+\frac{s}{500}\right)K_s
\]

is the dominant perspective-scaled linear term, and

\[
\begin{aligned}
O_s={}&2\cos K_s\\
&+\frac25\cos\left(5\left(x+\frac{s}{500}\right)K_s+8K_s\right)\\
&+\frac1{10}\cos\left(15\left(x+\frac{s}{500}\right)K_s-18K_s\right)
\end{aligned}
\]

is the oscillatory correction.

Because `|cos z| <= 1`, the correction has the analytic bound

\[
|O_s|\le 2+\frac25+\frac1{10}=2.5.
\]

This bound is included as a unit test.

The three cosine terms introduce progressively different phase structures. The important lesson is not simply that they are frequencies `1`, `5`, and `15`; their arguments are themselves modulated by `K_s(y)`, so the apparent spatial frequency changes strongly with `y`.

## 6. Run the study

```bash
python -m pip install -e '.[dev,visualization]'
pytest tests/unit/test_aurora_uvkq.py -q
python experiments/learning/studies/aurora_uvkq/render_uvkq.py
```

Generated diagnostics:

```text
figures/generated/learning/aurora_uvkq/01_U_perspective_coordinate.png
figures/generated/learning/aurora_uvkq/02_V0_perspective_coordinate.png
figures/generated/learning/aurora_uvkq/03_Ks_family.png
figures/generated/learning/aurora_uvkq/04_Q25_full_field.png
figures/generated/learning/aurora_uvkq/05_Q25_oscillatory_correction.png
```

## 7. Learning protocol

Before looking at each output, write a prediction for its zero sets, signs, singular behaviour, scale dependence, and oscillatory structure. Then compare the render with the prediction.

The first proficiency question is:

> Why does dividing by `y + 0.1001` create strong perspective-like compression and rapidly changing oscillation near one horizontal line?

Do not proceed to `J_s`, `A_nu`, or the final RGB construction until this question can be answered mathematically and visually.

## Scientific boundary

Classification: `mathematical-art / procedural-equation study`.

These equations are studied as visible generative mathematics. No claim is made that `U`, `V_nu`, `K_s`, or `Q_s` arise from magnetospheric plasma equations or atmospheric emission physics.
