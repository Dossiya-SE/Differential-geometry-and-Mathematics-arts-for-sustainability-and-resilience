# Interactive inversion laboratory — MSR-FIG-0002

**Status:** Proposed learning artifact; not accepted into the curated gallery.  
**Mathematics:** [`MSR-MOD-0002`](../../../mathematics/model_contracts/MSR-MOD-0002.json) · [derivation](../../../mathematics/derivations/MSR-DER-0002_sphere-inversion.md)  
**Authority:** Python reference [`msr.geometry.inversion`](../../../src/msr/geometry/inversion.py), not GLSL pixels.  
**Scientific domain and hazard:** `NOT_SELECTED`.

## What is being demonstrated?

Inversion `I(x)=r²x/||x||²` on `R²\{0}`, with radius controlled by a slider. Left panel: source Cartesian grid. Right panel: the image under inversion, plotted by inverse sampling. The blue outline denotes the fixed inversion circle. Animation changes a **visual parameter**, not physical time or a recovery trajectory.

The shader is original educational source inspired by procedural geometry and publicly available Shadertoy ideas; it is **not a copy of shader `4scfR2`**, whose implementation has not been verified.

## Open locally

Serve the repository root from a local static server:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/art/shaders/inversion_lab/`. Browser requires WebGL2; `static.svg` is the static reference and fallback. No CDN or external JavaScript dependencies are required.

## Learn by verifying

1. Hand-compute `I([2,0])=[0.5,0]` for `r=1`.
2. Verify `I(I(x))=x` and `||I(x)|| ||x|| = r²` using the Python reference.
3. Derive the Jacobian and prove `JᵀJ=(r⁴/||x||⁴)I`.
4. Change the radius slider; distinguish image deformation from source-coordinate motion.
5. Disable WebGL2 or open `static.svg`. The essential geometric statement must survive.
6. Test the actual GPU shader visually on different devices before promoting the figure.

```bash
PYTHONPATH=src python -m unittest tests.unit.test_inversion tests.properties.test_inversion_properties -v
python scripts/generate_inversion_static.py --check
```

## Visual encoding and limitations

- White canvas/panels; source and transformed grid lines use Light Sky Blue (`#87CEFA`); fixed inversion sphere uses Deep Sky Blue (`#00BFFF`); axes and panel divider have neutral distinguishable strokes.
- No color is used as the only meaning: left/right labels, axes, circle, mathematical caption and fallback remain available.
- The map is undefined only at the center, but shader rendering additionally excludes a small disk of radius `0.13` to avoid undersampling and extreme derivatives.
- WebGL2/highp, anti-alias derivatives, DPI and frame times depend on browser/device. Browser image verification and accessibility audit are pending.
- Reduced-motion preferences are respected by default (no automatic motion), and motion can be disabled by an explicit control.
- Mathematical verification is not external application validation, and a transformed grid is not evidence of resilience or sustainability performance.

**References:** Needham (1997), *Visual Complex Analysis*, chapter 3; <https://academic.oup.com/book/52945>. For Shadertoy/WebGL integration see <https://threejs.org/manual/pages/shadertoy.html>.
