# Viability boundary teaching animation — MSR-FIG-0004

**Status:** `PROPOSED_FOR_REVIEW`. **Class:** Explanatory dimensionless mathematics. **Domain:** `NOT_SELECTED`.

The autonomous system `x'(τ) = -x`, `τ>=0`, with initial state `x0∈R²`, has exact solution `x(τ)=e^{-τ}x0`. For `K={x:||x||<=1}`, the derivative `d||x||²/dτ=-2||x||²` is nonpositive; all states initially in K remain in K. Since no control or disturbance is defined, its viability kernel (with this declared autonomous dynamics and an all-future constraint) is simply K. A starting point outside K is **not** viable at its initial instant, despite potential later entry. This is a deliberately easy example, not a theorem about coupled infrastructure.

**Animation:** serve repository root using `python -m http.server 8000`, then open `http://localhost:8000/art/animations/viability_lab/`. Controls support manual seek, play/pause, reset; reduced-motion preference disables playback. The dimensionless time slider `0<=τ<=3` plays at a display rate, not physical time. If JavaScript is disabled, [static.svg](static.svg) shows the source state.

**Inputs:** A=(0.8,0.45), B=(1.4,0.35). B crosses the disk boundary when `τ=ln(||B||)`; mathematical entry does not retroactively grant viability. This is not a resilience service threshold, physical stressor, policy intervention, or recovery measurement.

**Verification:**
```sh
node --test art/animations/viability_lab/model.test.mjs
node art/visual_suite/render.mjs --check
```
Cross-browser timing, keyboard operation, focus and visual readability require independent review before gallery promotion. The code is version-controlled explanatory mathematics; it contains no empirical data.
