# Audit of the Primary-Evidence-Bundle Proposal

- Audit ID: `MSR-AUDIT-2026-08-22-01`
- Source audited: attached conversation record supplied by the project owner
- Repository state checked: `main`, 2026-08-22
- Scope: scientific logic, terminology, and the status of `MSR-CS-001`

## Conclusion

The proposal identifies a real weakness: a literature-review case cannot be called reproducible merely because the main PDF has been read. Claim-critical supplements, code, data, model dependencies, environment specifications, and execution evidence require explicit resolution. The proposal is therefore accepted in principle, with the revisions below.

## Determinations

| Proposal | Determination | Required revision |
|---|---|---|
| Maintain a primary evidence bundle for each computational paper | Accepted | Split source identity, artifacts, environment, experiments, and provenance instead of treating all entries as equivalent files. |
| Require every artifact class to resolve | Accepted with qualification | Resolution means a documented lifecycle outcome, not that every artifact exists or is accessible. Applicability is claim- and experiment-specific. |
| Use one Boolean gate over artifacts | Revised | The Boolean gate closes the artifact inventory only; it cannot certify execution, reproduction, or validation. |
| Use `DATA_NOT_REQUIRED` | Rejected as a generic label | Use `NOT_APPLICABLE` with a rationale tied to a named experiment. |
| Use `CODE_NOT_PUBLIC` when code cannot be found | Rejected without direct evidence | Use `NOT_FOUND_AFTER_SEARCH`; reserve restriction language for an identified artifact or explicit source statement. |
| Map equation to algorithm to code | Accepted | Add inputs, immutable code identifier, run command, tolerance, deviations, and output provenance. |
| Separate author result, reproduction, stress test, and interpretation | Accepted | Register each as a distinct stage with explicit pass criteria. |
| Store manifests and audit outputs instead of uncontrolled third-party payloads | Accepted | Record access and redistribution rights separately and preserve authoritative links and hashes. |
| Reopen `MSR-CS-001` | Accepted | Main-paper review remains complete, but artifact acquisition, implementation audit, execution, reproduction, and validation remain open. |

## Verified case-specific corrections

1. The official project page and the main paper identify `https://github.com/milmillin/d4descent` as the implementation repository.
2. Repository metadata and structure were inspected at commit `a66b729517a67b95330126bda7f84bb66a352aca`; this is not a semantic code audit.
3. The repository exposes Python 3.12, `pyproject.toml`, `uv.lock`, configurations, data directories, scripts, run assets, and source directories. The environment has not been built in this review.
4. The main paper refers to supplemental Theorem A.1, Algorithms 1 and 2, Appendix D, and additional supplemental material. No supplement asset was located in the documented search, so `NOT_FOUND_AFTER_SEARCH` is the defensible current status.
5. The reported counts 128, 25, and 23 describe benchmark subsets in the paper. They are not evidence that datasets were acquired or audited by this project.
6. No source-code execution, numerical reproduction, or independent stress test has been performed.

## Resulting status

`MSR-CS-001` is `MAIN_PAPER_REVIEWED__ARTIFACT_INVENTORY_OPEN__EXECUTION_NOT_STARTED`.

This case remains valuable as a transferable method and mathematical-form case (`M+G+V`). It does not directly establish differential geometry, sustainability performance, resilience performance, or a preferred application domain.
