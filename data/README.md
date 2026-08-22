# Data policy

The repository does not currently contain an application dataset. The application remains `NOT_SELECTED`.

## Local directories

- `raw/`: immutable source files retained locally, never silently edited;
- `processed/`: deterministic transformations of identified raw inputs;
- `external/`: third-party reference data not owned by the project.

The contents of these directories are ignored by Git by default. A committed data record must state source, acquisition date, license, access conditions, schema, units, spatial and temporal coverage, transformations, privacy and safety assessment, known quality limitations, and SHA-256 checksum.

Large files should use an external research archive, object store, or data-versioning system. Source papers are referenced by DOI and checksum rather than redistributed without permission.
