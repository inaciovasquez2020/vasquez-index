# Vasquez Index

Public front door for the Unified Rigidity Framework (URF).

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

## Links

- GitHub profile: https://github.com/inaciovasquez2020
- ORCID: https://orcid.org/0009-0008-8459-3400
- Research site: https://vasquezresearch.com
