# Lesson 0001: Install and verify the inversion shader demonstration

This file accompanies the proposed lesson in issue #25. The change is **not** a model of infrastructure resilience or a selection of an application domain.

## Learning sequence

1. Read `mathematics/derivations/MSR-DER-0002_sphere-inversion.md` and manually prove involution and conformality.
2. Read `src/msr/geometry/inversion.py` and explain why `x=c`, zero radius, and underflow are rejected.
3. Run the deterministic Python numerical and artifact tests.
4. Inspect the browser experience using `art/shaders/inversion_lab/index.html`. Compare original versus inverted coordinates.
5. Record device, browser version, screenshots, rendering deficiencies and accessibility observations before interpreting GPU output.
6. Only after the geometry lab has passed, consider a separately specified domain-neutral signed-distance/viability-boundary visualization. Do not use an inverted grid as a depiction of physical resilience by analogy.

## Applying these additive files to the full repository

Extract the package into the **root** of the cloned repository, preserving subdirectories, after reviewing its contents.

```bash
python scripts/generate_inversion_static.py --check
PYTHONPATH=src python -m unittest discover -s tests -v
python scripts/generate_manifest.py --write
make verify
# With the repository dev dependencies installed:
make verify-ci
python -m http.server 8000
```

Then open `http://localhost:8000/art/shaders/inversion_lab/`. Do not merge before reviewing the browser shader on real devices. The integrity manifest is required by the repository: compute it from the entire checkout after introducing these files. It is intentionally not shipped as a partial replacement in the package.

The source shader for Shadertoy ID `4scfR2` was unavailable for direct code inspection. The implementation here is original and does not reproduce or claim verification of that specific shader.
