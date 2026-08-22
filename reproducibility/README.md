# Reproducibility

Reproducibility records the complete path from a versioned model and experiment to tests, figures, documentation, and release artifacts.

| Object | Current control |
|---|---|
| Python dependencies | Compatible ranges in `pyproject.toml`, verified direct constraints, and an observed full-environment snapshot |
| Operating-system environment | `containers/Dockerfile` and `.devcontainer/devcontainer.json` |
| Experiment seed and precision | Registered experiment JSON |
| Repository integrity | `MANIFEST.sha256` |
| Automated reproduction | `.github/workflows/reproducibility.yml` |

A future release should add resolved lockfiles and archive identifiers. Reproducibility is reported as a status with limitations; it is never assumed from the presence of code alone.
