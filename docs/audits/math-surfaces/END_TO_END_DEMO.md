# Mathematics-surface engineering: audited end-to-end demonstration

**Audit date:** 2026-08-22  
**Evidence state:** `VERIFIED_WITH_DECLARED_LIMITATIONS`  
**Uploaded source SHA-256:** `62af3307691dec2cb905fde739a23ec08dc51a9a50a1c8aefecab2d364ec6917`  
**Revalidation tool:** `engineer-math-surfaces 1.3.0`

## 1. Scope and identity

This document audits and supersedes the uploaded `END_TO_END_DEMO(1).md`. The uploaded report describes an isolated mixed-surface fixture; it is not evidence about this sustainable-resilience repository unless a result is independently rerun here.

The fixture is preserved in [the Git bundle](evidence/end-to-end-demo/math-surface-demo.bundle) and can be reconstructed without relying on an unversioned working directory.

| Fixture state | Immutable commit |
|---|---|
| Controlled baseline | `ca2029c660b3bfd3b55736b638cd26828c0f18f8` |
| Repairs and governance | `230cf578163c03590d0d0058e39712d9002ebf08` |
| Final report alignment | `6503de2006c7d08994e8e08c6bd0a55515e5be4e` |

The fixture contains GitHub Markdown, archival Markdown, MDX, Quarto, LaTeX, Jupyter, generated HTML, literal code examples, and currency.

## 2. Governing contracts

| Authority | Role in this audit |
|---|---|
| [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions) | Defines supported inline, block, and fenced-math containers and confirms GitHub's use of MathJax |
| [`github/cmark-gfm`](https://github.com/github/cmark-gfm) | Supplies the pinned GFM structural oracle |
| [Pandoc mathematics](https://pandoc.org/MANUAL.html#math) | Defines extension-dependent conversion behavior |
| [Quarto equations](https://quarto.org/docs/authoring/markdown-basics.html#equations) | Defines the native Quarto source contract |
| [MathJax accessibility components](https://docs.mathjax.org/en/latest/web/components/accessibility.html) | Governs semantic enrichment, speech, exploration, and assistive output |
| [KaTeX options](https://katex.org/docs/options) | Governs strict parsing, error handling, trust, and MathML output |
| [Playwright snapshots](https://playwright.dev/docs/test-snapshots) | Governs deterministic visual-regression conditions |

## 3. Baseline findings reproduced

Skill version `1.3.0` reproduced the uploaded baseline exactly:

| Rule | High confidence | Review | Meaning |
|---|---:|---:|---|
| `MSM001` | 2 | 1 | Two active and one archival legacy inline delimiter |
| `MSM002` | 2 | 0 | Two active legacy display delimiters |
| `MSM003` | 0 | 1 | One raw-TeX intent candidate |
| `MSM010` | 1 | 0 | One display consumed as GFM Setext structure before math rendering |
| **Total** | **5** | **2** | Seven findings in three files |

Raw evidence: [baseline-audit.json](evidence/end-to-end-demo/baseline-audit.json).

## 4. Claim-by-claim audit of the uploaded report

| Uploaded claim | Disposition | Why |
|---|---|---|
| Two active inline and two active display legacy repairs | `VERIFIED` | Baseline findings, committed diff, deterministic dry run, and final source agree |
| One `MSM010` container repair | `VERIFIED` | The original `$$` body was converted to fenced `math`; its TeX-body hash is unchanged |
| Raw prose TeX required manual adjudication | `VERIFIED` | The fixer correctly refused `MSM003`; the complete expression was manually wrapped |
| Archival quotation was preserved | `VERIFIED` | Its committed blob and reported whole-file hash are unchanged |
| Literal currency required explicit escaping | `VERIFIED` | The committed diff preserves `125` and `2,400` while removing delimiter ambiguity |
| LaTeX required `amsmath` | `VERIFIED` | The committed diff adds the package; `pdflatex` now completes |
| Ten intended formulas were extracted | `VERIFIED` | The new extraction inventory contains exactly ten records |
| Quarto source via Pandoc produced two MathML nodes | `VERIFIED_LIMITED` | Pandoc `3.1.3` ran; the Quarto CLI itself was unavailable |
| Notebook via Pandoc produced two MathML nodes | `VERIFIED_LIMITED` | Notebook JSON parsed and two MathML nodes were emitted |
| `cmark-gfm` was unavailable | `HISTORICAL_ONLY` | It was true for the first run; exact version `0.29.0.gfm.13` was subsequently built and executed |
| MathJax and KaTeX were unavailable | `HISTORICAL_ONLY` | Exact dependencies were subsequently installed and all ten formulas passed both engines |
| MDX compiler was uninspected | `UNCHANGED_LIMITATION` | The fixture declares no project MDX compiler or plugin configuration |
| Hosted GitHub fixture was uninspected | `UNCHANGED_LIMITATION` | The fixture is an isolated bundle, not a hosted repository |
| Visual regression was unexecuted | `UNCHANGED_LIMITATION` | No reviewed baseline exists in a pinned browser image |

## 5. Tool defects discovered and corrected

### 5.1 Provenance gap

Version `1.2.0` recorded legacy-delimiter bodies but not the `MSM010` body automatically. Version `1.3.0` now computes the body hash before and after conversion, requires equality, records `byte_identical: true`, and stops instead of writing when equality cannot be proved.

The fixture repair now records:

- before SHA-256: `f4dfc991f907c9a891657cc914ccd39252d8d201e2e41b709ee1a667e865ea72`;
- after SHA-256: `f4dfc991f907c9a891657cc914ccd39252d8d201e2e41b709ee1a667e865ea72`;
- equality: `true`.

Raw evidence: [repair-ledger.json](evidence/end-to-end-demo/repair-ledger.json).

### 5.2 Structural-comparison false failure

The earlier comparator included `sourcepos` metadata. Delimiter-length changes necessarily alter those positions, and an `MSM010` repair intentionally turns a wrongly parsed heading into a math container. The old implementation therefore failed valid repairs.

Version `1.3.0` now:

1. normalizes only complete recognized display-math containers;
2. preserves non-math code fences;
3. excludes unstable source-position metadata;
4. enables the GFM extensions in the pinned parser;
5. still rejects non-mathematical heading and document-structure changes.

With `cmark-gfm 0.29.0.gfm.13` at commit `587a12bb54d95ac37241377e6ddc93ea0e45439b`, the corrected comparison preserves 59 README nodes and 11 model-document nodes. Raw evidence: [cmark-readme.txt](evidence/end-to-end-demo/cmark-readme.txt) and [cmark-model.txt](evidence/end-to-end-demo/cmark-model.txt).

## 6. Revalidated verification matrix

| Gate | Result | Evidence |
|---|---|---|
| Dry run before apply | `PASS` | Dry-run and applied patches share SHA-256 `02661b08f82503acc95ab75acf1142e459385bc2142529f04c5721317c7c2618` |
| Post-fix audit | `PASS_WITH_EXPECTED_REVIEW` | One archival review item; zero high-confidence findings |
| Regression suite | `PASS` | 25/25 tests, including pinned cmark integration and pre-commit untracked-file discovery tests |
| `MSM010` semantic preservation | `PASS` | Matching pre/post body hashes and `byte_identical: true` |
| Formula extraction | `PASS` | Ten intended formulas |
| MathJax 4 | `PASS` | 10/10 with version `4.1.3` |
| Strict KaTeX | `PASS` | 10/10 with version `0.18.4` |
| GFM structural parity | `PASS` | 59 and 11 nodes preserved in the two repaired Markdown documents |
| LaTeX | `PASS` | `pdflatex` produced one page |
| Quarto source through Pandoc | `PASS_LIMITED` | Two MathML nodes; native Quarto unexecuted |
| Notebook through Pandoc | `PASS_LIMITED` | Two MathML nodes |
| MDX | `UNINSPECTED` | No declared compiler |
| Hosted fixture | `UNINSPECTED` | No hosted target |
| Visual baseline | `UNEXECUTED` | No reviewed pinned-environment baseline |

Raw renderer evidence: [renderer-validation.json](evidence/end-to-end-demo/renderer-validation.json). Final scanner evidence: [final-audit.json](evidence/end-to-end-demo/final-audit.json). Formula evidence: [math-fragments.json](evidence/end-to-end-demo/math-fragments.json).

## 7. Reproduction

From this directory:

```bash
git clone evidence/end-to-end-demo/math-surface-demo.bundle demo
git -C demo fsck --full
git -C demo checkout ca2029c660b3bfd3b55736b638cd26828c0f18f8
```

Run the current scanner against the baseline, inspect the dry-run patch, apply in an isolated clone, and then check out the final fixture commit for native-surface and renderer validation. Verify every retained artifact with [SHA256SUMS](evidence/end-to-end-demo/SHA256SUMS).

Do not apply the fixture's repair commit to another repository. Transfer the method and gates, not the fixture content.

## 8. Release decisions

### Fixture

The validated subset passes syntax, semantic-body preservation, strict dual rendering, GFM structural parity, LaTeX, Pandoc Quarto-source conversion, and notebook conversion. A universal claim covering every declared surface remains **blocked** because MDX, native Quarto, hosted fixture rendering, and the visual baseline are not all executed.

### Sustainable-resilience repository

The fixture's decision is not inherited. This repository remains domain-neutral with application state `NOT_SELECTED`. Its own mathematics-surface audit, renderer inventory, GitHub Actions, and hosted rendering determine whether [PR #15](https://github.com/Dossiya-SE/Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience/pull/15) is ready for review.
