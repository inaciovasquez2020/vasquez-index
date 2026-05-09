# Vasquez Index

<!-- VERIFIED_FRONTIER_TRACKING_DOOR:BEGIN -->
## Verified Frontier Tracking

# Vasquez Index — Current reference Registry Dashboard
Vasquez Index is the public front door for **Verified Frontier Tracking**: an AI-readable, publicly checkable system for hard research claims.

Its role is to route readers to the correct layer:

| Layer | Repository | Role |
|---|---|---|
| Public index | `vasquez-index` | Start-here map and canonical navigation |
| Transparency proof | `frontier-status-dashboard` | CI health, integrity, theorem-boundary status, and review readiness |
| Explanation | `urf-textbook` | Human-readable exposition and release-facing documentation |
| Definitions | `urf-core` | Trusted definitions, schemas, and verification artifacts |
| Technical demonstration | `chronos-urf-rr` | Executable URF/Chronos frontier implementation |

Boundary: this index is a navigation and status surface. It does not claim theorem-level closure unless a linked artifact explicitly names and proves that closure.
<!-- VERIFIED_FRONTIER_TRACKING_DOOR:END -->

## Purpose
To provide a single current reference registry of enabled repositories, stable references, and reproducibility links.

## Current referenceity & Governance
This repository operates under the **Current referenceity Doctrine** of the Vasquez Research Program.
All structural claims, artifact-backed proofs, and publication statuses are governed by a single status-locked document:
Public front door and registry index for the Unified Rigidity Framework (URF).
This repository is the public registry surface for the small set of active public URF repositories.
## Start here
URF is a verification-first research program for organizing rigidity principles, locality constraints, entropy/capacity bounds, formal proof surfaces, executable certificates, and claim-status discipline.

## What URF is not

URF does not claim theorem-level closure of any major open problem unless the relevant repository explicitly states and verifies that closure.

## Public repository set

| Repo | Role |
|---|---|
| `inaciovasquez2020` | GitHub profile README and public orientation |
| `vasquez-index` | Public front door and repository map |
| `urf-core` | Core reference layer |
| `chronos-urf-rr` | Reference executable/verification implementation |
| `urf-textbook` | Expository layer |
| `frontier-status-dashboard` | Public status dashboard |

## Private / archived work

Source:
https://github.com/inaciovasquez2020/current terminal-wall-fo-k-locality/blob/main/docs/local-global-barrier.tex
Additional experimental, frontier, application, and Clay-adjacent repositories are private or archived pending review, preprint release, or external validation.

## Status classes

| Class | Meaning |
|---|---|
| Verified | Repository checks, CI, formal files, and stated certificates pass. |
| Conditional | A result depends on explicitly named assumptions or external theorem inputs. |
| Open | A named obstruction/frontier remains unresolved. |
| Not claimed | Build success, dashboard status, or executable evidence does not imply theorem-level closure. |

## Dependency diagram

    vasquez-index
       |
       +-- urf-core
       |      |
       |      +-- chronos-urf-rr
       |
       +-- urf-textbook
       |
       +-- frontier-status-dashboard

## Verification principle

Build PASS means repository verification passed. It does not mean theorem-level closure unless the relevant repository explicitly states and verifies theorem-level closure.

```bibtex
@manual{Vasquez_Index_2026,
  author = {Vasquez, Inacio F.},
  title  = {Vasquez Index: Current reference Repository Registry and Dashboard},
  year   = {2026},
  url    = {[https://inaciovasquez2020.github.io/vasquez-index/](https://inaciovasquez2020.github.io/vasquez-index/)}
}

Structural wrappers
- Cyclone (terminal obstruction): https://github.com/inaciovasquez2020/cyclone-terminal-obstruction
- Whiplash (stability checks): https://github.com/inaciovasquez2020/whiplash-stability
- Capacity-Locality-Certification: https://github.com/inaciovasquez2020/capacity-locality-certification
- Reductions map: https://github.com/inaciovasquez2020/urf-reductions-sat-csp
- Docs source: https://github.com/inaciovasquez2020/vasquez-docs
---
## Registry
This repository is part of the URF registry.
See:
- `REGISTRY.md` for status-locked role and scope declarations.
## External status
This repository is governed by [`docs/status/EXTERNAL_STATUS_LOCK.md`](docs/status/EXTERNAL_STATUS_LOCK.md). Build success, CI success, dashboards, ledgers, axioms, admits, `sorry`, or placeholder witnesses do not constitute theorem-level closure.
## Lean proof portfolio classification
This repository is governed by [`docs/status/LEAN_PROOF_PORTFOLIO_CLASSIFICATION.md`](docs/status/LEAN_PROOF_PORTFOLIO_CLASSIFICATION.md). Its role in the portfolio is explicitly classified as proof-facing, conditional frontier, infrastructure/documentation, or legacy/scaffold.
## Links
- GitHub profile: https://github.com/inaciovasquez2020
- ORCID: https://orcid.org/0009-0008-8459-3400
- Research site: https://vasquezresearch.com

## Formal Status

Status: Documentation / Index Surface

It does not independently prove mathematical claims.

Every theorem-level claim must inherit from a buildable formal source repository.

`docs/status/SOURCE_OF_TRUTH_2026_04_27.md`
