# Mathematical Visual Design Studio — V0.1

A governed UI prototype for designing mathematical and scientific visuals from a common Visual IR.

## Implemented now

- React + TypeScript interface
- common Visual IR 0.1.0
- Three.js/WebGL live differential-geometry preview
- generated Python / TypeScript / GLSL / LaTeX source views from the same object
- scientific validation gates for a curvature-coded torus
- Python adapter for downstream scientific computation
- epistemic status preserved as part of the object model

The demonstrator uses the regular torus

`X(u,v)=((R+r cos v) cos u,(R+r cos v) sin u,r sin v)`

with analytic Gaussian curvature

`K(v)=cos(v)/(r(R+r cos(v)))`.

Validation checks `R > r > 0`, finite sampled curvature, and metric regularity `EG-F^2 > 0`. The object remains explicitly `ILLUSTRATIVE`; rendering quality does not convert it into empirical evidence.

## Run

```bash
npm install
npm run check
npm run dev
```

V0.1 intentionally implements the first production subset. The Visual IR is the stable boundary for future PyVista/VTK, Manim, Blender, TikZ/Asymptote, WGSL/WebGPU, Julia/Makie, and Rust/WASM adapters.
