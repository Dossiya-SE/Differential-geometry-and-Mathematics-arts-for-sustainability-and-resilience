# Mathematical Visual Design Studio — Skill Catalog V0.3

This catalog defines the computational and visual-engineering skills that the desktop studio should expose through one GUI while keeping each task attached to the engine best suited to it.

## Implemented native skills

| Skill | Primary engine | Current state |
|---|---|---|
| Parametric-surface rendering | Three.js / WebGL | Implemented |
| Gaussian-curvature visual encoding | Visual IR + Three.js | Implemented |
| Mathematical validation | TypeScript validation layer | Implemented |
| Python code execution | Tauri / Rust -> Python | Implemented |
| JavaScript code execution | Tauri / Rust -> Node.js | Implemented |
| Julia code execution | Tauri / Rust -> Julia | Implemented when Julia is installed |
| Generated SVG/PNG/JPEG/WebP preview | Native workspace bridge | Implemented |
| Scientific Python environment management | Python venv + pip from GUI | Implemented |
| Runtime/tool detection | Tauri / Rust | Implemented |
| Exact equation typography | KaTeX | Implemented |
| Generated Python/TypeScript/GLSL/LaTeX views | Visual IR code generation | Implemented |

## Scientific Python skills available through one-click profiles

- numerical arrays and linear algebra — NumPy;
- integration, optimization, interpolation, signal processing and statistics — SciPy;
- symbolic algebra, differentiation, simplification and exact equations — SymPy;
- scientific plotting and publication figures — Matplotlib;
- graph/network mathematics — NetworkX;
- tabular data workflows — pandas;
- interactive plotting — Plotly;
- VTK-backed geometry, meshes, scalar/vector fields and scientific 3D — PyVista + VTK;
- automatic differentiation and accelerated numerical kernels — JAX;
- mathematical animation — Manim Python package.

## External-engine skills detected by the Runtime Manager

- Blender / Geometry Nodes / Blender Python — cinematic 3D and high-end geometry rendering;
- Manim CLI — mathematical animation pipelines;
- FFmpeg — video encoding and animation post-processing;
- Tectonic — reproducible LaTeX/PDF compilation;
- Asymptote — precise mathematical vector and 3D diagrams;
- Graphviz — graph layout and dependency visualizations;
- Julia — high-performance numerical computing and future Makie rendering.

Detection does not mean that every external adapter is already exposed as a one-click render action. The GUI must distinguish `READY`, `DETECTED`, `ADAPTER_IMPLEMENTED`, and `PLANNED` rather than claiming capabilities that are not wired end-to-end.

## Next adapter skills

1. PyVista scene -> Visual IR -> Three.js exchange.
2. Manim scene generation and MP4 preview inside the app.
3. Blender Python / Geometry Nodes scene generation and render import.
4. TikZ/Tectonic and Asymptote publication-render adapters.
5. Julia/Makie plot and geometry adapter.
6. WGSL/WebGPU compute and field renderer.
7. Rust/WebAssembly numerical kernels.
8. Project-level file Open/Save/Export with reproducible manifests.
9. Visual node editor: Domain -> Equation -> Geometry -> Differential Operator -> Visual Mapping -> Renderer.
10. Sandboxed execution mode for untrusted code.

## Governing rule

No engine is included only because it is powerful. Each engine must have a defined mathematical/visual role, a reproducible input/output contract, provenance, validation, and a clear epistemic boundary.
