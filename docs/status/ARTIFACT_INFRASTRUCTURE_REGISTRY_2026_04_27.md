# Artifact Infrastructure Registry — 2026-04-27

Status: Cross-Repo Artifact Infrastructure Registry

Scope: repository infrastructure only.

This registry records artifact-infrastructure status across the active portfolio. It does not assert theorem-level completion, external validation, publication acceptance, or mathematical closure.

## Taxonomy

| Label | Meaning |
|---|---|
| `Audited` | Repository has an explicit status/audit surface and verifier. |
| `Certified Frontier` | Repository has a certified executable or documented frontier boundary. |
| `Conditional` | Repository contains conditional mathematical claims that must remain labeled. |
| `Experimental` | Repository is exploratory and should not be read as a completed theorem surface. |
| `Archived` | Repository is inactive or preserved for record only. |

## Registry

| Repository | Artifact infrastructure status | Mathematical status | External validation status | Required next artifact |
|---|---|---|---|---|
| `vasquez-index` | Audited | Unchanged | Unchanged | Maintain source-of-truth registry |
| `poincare-new-derivation` | Audited | Unchanged | Unchanged | Keep artifact-status verifier green |
| `pachner-invariant` | Certified Frontier | Unchanged | Unchanged | Keep Lean frontier classification explicit |
| `clay-problem-lab` | Certified Frontier | Conditional / Frontier | Unchanged | Keep RA1n boundary and no-overclaim verifier green |
| `ym-os-quantization` | Certified Frontier | Conditional / Frontier | Unchanged | Keep OS-positive-measure frontier explicit |
| `chronos-urf-rr` | Audited | Conditional / Frontier | Unchanged | Keep status snapshot and verification path current |
| `urf-core` | Audited | Framework / Conditional | Unchanged | Keep theorem hierarchy separated by status |
| `urf-textbook` | Audited | Expository | Unchanged | Keep public start-here path current |

## Stop rule

The portfolio artifact-infrastructure layer is not complete unless every active repository has:

1. a status or scope document;
2. a verifier or test for status claims;
3. an explicit boundary against theorem-level overclaiming;
4. a release, closure, or frontier manifest when applicable;
5. a classification under this registry.

## Boundary

This registry does not upgrade any repository to solved, accepted, published, peer reviewed, externally validated, or mathematically closed.

