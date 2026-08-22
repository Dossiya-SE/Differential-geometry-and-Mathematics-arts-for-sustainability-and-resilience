# Validation and Provenance Log

## Review identity

- Review ID: `MSR-CS-001`
- Review version: `0.3.0`
- Verification date: `2026-08-22`
- Reviewer: Dossiya Dakou
- Review type: focal-paper critical transfer review
- Current stage: `MAIN_PAPER_REVIEWED__ARTIFACT_INVENTORY_OPEN__EXECUTION_NOT_STARTED`
- Source manifest: [`SOURCE_MANIFEST.yaml`](SOURCE_MANIFEST.yaml)

## Source identity

- Title: *Design for Descent: What Makes a Shape Grammar Easy to Optimize?*
- Authors: Milin Kodnongbua, Zihan Jack Zhang, Nicholas Sharp, Adriana Schulz
- Venue: SIGGRAPH Asia 2025 Conference Papers
- DOI: `10.1145/3757377.3764004`
- Official project page: `https://www.computationaldesign.group/publications/design-for-descent`
- Main-paper pages: 11
- PDF size: 5,873,001 bytes
- PDF SHA-256: `9b61925d981edf9173aa58045bf90e44488e09e5ded1c692085f75a9e0812314`
- Encryption: none
- JavaScript: none
- Forms: none

## Official implementation identity

- Repository: `https://github.com/milmillin/d4descent`
- Provenance: linked by the official project page and stated in the main paper
- Pinned commit: `a66b729517a67b95330126bda7f84bb66a352aca`
- Pinned tree: `7e5ba7cf9f541da09b236f4fc6eb71a28eb8ee5b`
- Commit date: `2025-09-24`
- Inspection boundary: repository identity, top-level structure, README, Python version, dependency specification, lock-file presence, and selected configuration/data directory metadata
- Environment built: no
- Implementation semantics audited: no
- Source code executed: no

## Verification actions

| Check | Result |
|---|---|
| PDF metadata inspected | PASS |
| All 11 main-paper pages text-extracted | PASS |
| Abstract and bibliographic metadata checked | PASS |
| Equations in Section 3 inspected | PASS |
| Table 1 grammar properties inspected | PASS |
| Tables 2 and 3 inspected | PASS |
| Figures on PDF pages 1, 4, 6, and 9 visually inspected | PASS |
| Limitations and conclusion inspected | PASS |
| Official code provenance resolved | PASS |
| Code repository metadata and top-level structure inspected at pinned commit | PASS |
| Python version and dependency/lock-file presence inspected | PASS |
| Supplemental artifact located | NO — `NOT_FOUND_AFTER_SEARCH` |
| Code environment built | NO — `NOT_STARTED` |
| Source code executed | NO — `NOT_STARTED` |
| Numerical results independently reproduced | NO — `NOT_STARTED` |
| Independent stress test performed | NO — `NOT_STARTED` |
| Former six-chain crosswalk replaced with the ten-chain `MSR-CA-001` mapping | PASS |
| Case-study Markdown and YAML contain all ten unique chain identifiers | PASS |

## Supplemental search boundary

The main paper refers to supplemental Theorem A.1, Algorithms 1 and 2, Appendix D, and additional figures and tables. On 2026-08-22 the official project page, official main-paper PDF, ACM DOI/full-article landing pages, and official code-repository root and documented links were checked. No supplement asset was located.

The current status is `NOT_FOUND_AFTER_SEARCH`. It must not be rewritten as `not public` or `does not exist` without direct evidence.

## Claim controls

1. The paper is classified `M+G+V`, not direct application `D`.
2. The words *geometry*, *topology optimization*, and *shape space* are not treated as evidence of differential geometry.
3. Structural weight reduction is not treated as a complete sustainability assessment.
4. Computational repairability is not treated as physical infrastructure recoverability.
5. The stratified hybrid transfer abstraction is labeled `PROPOSED`.
6. No global absence claims are made from the focal paper.
7. No application domain, hazard, geography, outcome, or demonstrator is selected from this focal paper.
8. Evidence for one link is not treated as evidence for a complete chain or its endpoint.
9. Structural weight is recorded under C08 only as partial method context; sustainability remains `NOT_OBSERVED`.
10. Mathematical form generation under C10 is separated from untested comprehension, participation, behavioral, and decision effects.
11. Code identification and metadata inspection are not treated as implementation audit, execution, or reproduction.
12. The reported benchmark counts 128, 25, and 23 are not treated as acquired or audited datasets.

## Open reproduction requirements

1. Locate or obtain the supplement, or document a later terminal access state.
2. Complete equation-to-algorithm-to-code mapping at the pinned commit.
3. Inventory claim-critical data files, provenance, licenses, and hashes.
4. Resolve pretrained-model identifiers and access requirements for SDS experiments.
5. Declare target figures/tables, metrics, tolerances, seed policy, hardware, and run commands before execution.
6. Build the pinned environment and preserve the build log.
7. Execute registered experiments and preserve raw outputs.
8. Compare outputs with the paper using predeclared tolerances.
9. Separate reproduction results from later stress tests and project interpretation.

## Completion determination

The main-paper critical review is complete at its declared scope. The primary artifact inventory is not closed because data and model resolution remain incomplete; the supplement ended the documented search at `NOT_FOUND_AFTER_SEARCH`. Environment construction, execution, numerical reproduction, and independent validation have not begun. The case must not be described as fully reviewed or reproduced.
