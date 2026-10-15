# URF Repository Registry

This index records the **role, scope, and authority level** of repositories
within the Unified Rigidity Framework (URF).

Only repositories listed here are considered registry-visible.

---

## Core Theory & Invariants

### Chronos–EntropyDepth
- **Repo:** https://github.com/inaciovasquez2020/Chronos-EntropyDepth
- **Role:** Canonical invariant specification
- **Authority:** Normative
- **Scope:** Entropy-Depth definitions, bounds, structural obstructions
- **Executable:** No (documentation-first)
- **Status:** Private repository (current GitHub metadata); specification completeness and reproducibility are not externally auditable from the public index.

---

## Reference Implementations

### chronos-urf-rr
- **Repo:** https://github.com/inaciovasquez2020/chronos-urf-rr
- **Role:** Reference implementation
- **Authority:** Non-normative
- **Scope:** Executable validation of Chronos logic
- **Executable:** Yes
- **Status:** Registry-aligned

---

## Composition & Infrastructure

### Legacy entry: urf-prefab-system (unresolved)
- **Previously recorded repo:** https://github.com/inaciovasquez2020/urf-prefab-system
- **Role recorded historically:** Canonical prefab definitions
- **Audit result (2026-10-15):** GitHub API returned 404 and the name was absent from the current account repository listing.
- **Status:** Unverified legacy entry; do not treat as a current canonical dependency until its identity and location are restored or explicitly retired.

---

## Upstream Framework

### urf-core
- **Repo:** https://github.com/inaciovasquez2020/urf-core
- **Role:** Framework axioms and admissibility rules
- **Authority:** Normative
- **Status:** Frozen

## Chronos PR233 dashboard sync — 2026-05-12

The public status surface has been synchronized with the merged Chronos and dashboard updates:

- `chronos-urf-rr` PR #231: RepositoryNativeZeroArityInterface closure.
- `chronos-urf-rr` PR #232: zero-arity exhaustiveness to Reg-SNF bridge.
- `chronos-urf-rr` PR #233: current unrestricted Reg-SNF status lock.
- `frontier-status-dashboard` PR #50: dashboard row updated.

Dashboard state:

- Repository integrity: 100%.
- Theorem closure: 82%.
- Current real Chronos-admissible unrestricted Reg-SNF: status-locked closed.
- Selected DepthBridge reachability: locked.

Boundary preserved: no UniversalFiberEntropyGap closure, no DepthBridge beyond selected final carrier domain, no Chronos-RR theorem-level closure, no H4.1/FGL theorem-level closure, no P vs NP closure, and no Clay-problem closure.

## URC public demo container pointer — 2026-06-25

- Repository: `inaciovasquez2020/URC`
- Merge commit: `1254de0466cbed8f5ed80dd4e116d7505e11aa15`
- PR: `inaciovasquez2020/URC#6`
- Scope: implementation remains in `URC`; this index entry is a pointer only.
- Public demo package: `ghcr.io/inaciovasquez2020/urc-public-demo` (published; visibility confirmed public on 2026-06-25).
- Private-by-default package boundary: do not recreate or publish `ghcr.io/inaciovasquez2020/urc`.
- `urf-templates`: unchanged.

## URF SG verifier container pointer — 2026-06-25

- Repository: `inaciovasquez2020/urf-core`
- Package: `ghcr.io/inaciovasquez2020/urf-sg-verifier`
- Visibility: public; confirmed by GitHub Packages on 2026-06-25.
- Install: `docker pull ghcr.io/inaciovasquez2020/urf-sg-verifier:latest`
- Scope: public verifier/demo container pointer only; implementation remains in `urf-core`.
- Boundary: this index entry does not claim theorem-level closure or external validation beyond explicit repository/package artifacts.


## Registry audit — 2026-10-15

This audit records repository visibility and link resolution, not mathematical validity.

| Entry | Observed condition | Disposition |
|---|---|---|
| `Chronos-EntropyDepth` | Repository currently private | Retained as a private normative specification pointer; external readers cannot independently inspect it through the public index. |
| `chronos-urf-rr` | Public repository; release endpoint returns a release entry | Implementation pointer resolves. Release presence does not establish theorem closure. |
| `urf-prefab-system` | Repository endpoint returned 404 and name absent from current account listing | Marked unresolved legacy entry above; canonical status withdrawn pending identity resolution. |
| `urf-core` | Public repository; release endpoint returns an entry labeled `untagged-...` | Repository pointer resolves; stable version-tag and artifact reproducibility requirements need separate audit. |
| `URC` | Repository currently private | Implementation remains a private pointer; public demo package is a separate distribution surface. |

The current account listing contains 70 repositories, of which 19 are public. The public inventory in `README.md` enumerates those 19. The public navigation page must not present private repositories as publicly accessible.

**Audit boundary:** this is a targeted registry/link/visibility audit, not a repository-by-repository verification of every release, artifact hash, proof, or scientific claim. No theorem-level status is upgraded by this audit.


## Release and historical-pointer cross-check — 2026-10-15

| Pointer | Observed evidence | Boundary |
|---|---|---|
| Chronos PRs #231, #232, #233 | All three GitHub pull requests are closed and merged on 2026-05-12. | Confirms merge history only; the theorem scope remains the scope stated in the source repository. |
| Frontier dashboard PR #50 | Closed and merged on 2026-05-12. | Confirms the dashboard update was merged, not that dashboard metrics establish mathematical closure. |
| `frontier-status-dashboard` | Public release entries `zenodo-2026-05-26` and `zenodo-2026-05-26-r2` resolve. | A historical registry snapshot reports “Theorem closure: 82%”. This audit did not establish the metric's denominator, semantics, or validation protocol. Do not interpret it as a percentage of a theorem proved or of science completed. |
| `urf-templates` | Public release `v0.1.0` resolves. | Release presence establishes a published version pointer, not general scientific-claim validation. |
| `urf-verifier` | Public releases `v1.0.0`, `v1.1.0`, and `uv-vbc-1-2026-04-26` resolve. | Verifier success is limited to the certificate and provenance checks actually implemented. |
| `urf-spine-public` | Public repository resolves; no GitHub releases were returned by the releases endpoint. | No release artifact was verified in this pass; absence of a release is not itself a proof defect. |
| `vasquez-index` | Release `vi-ibc-1-2026-04-26` resolves; PRs #46 and #47 are merged. | Release and PR records verify repository history and index changes, not the completeness of the research portfolio. |

**Remaining unverified:** a complete per-repository audit of artifact hashes, pinned commit/tag references, reproduction instructions, formal proof dependencies, and current theorem claims across all 19 public repositories and the private research repositories. The public index is now a visibility-correct navigation map; it is not a certificate that the underlying portfolio is complete.


## Public release coverage snapshot — 2026-10-15

The GitHub Releases endpoint was queried for each of the 19 public repositories. Up to three recent release entries are recorded in `artifacts/public-repository-inventory.json`. The table below summarizes the observed endpoint results.

| Repository | Observed release metadata | Interpretation |
|---|---|---|
| [`biological-friction-framework`](https://github.com/inaciovasquez2020/biological-friction-framework) | Release entries returned: `frozen-2026-02-13`, `canonical-examples-v1`, `v1.0` | Release metadata observed; assets and reproducibility not audited |
| [`chronos-urf-rr`](https://github.com/inaciovasquez2020/chronos-urf-rr) | Release entries returned: `zenodo-2026-05-26`, `v_ack_vardi`, `urf-classification-freeze-2026-04-01` | Release metadata observed; assets and reproducibility not audited |
| [`cslib-fmt`](https://github.com/inaciovasquez2020/cslib-fmt) | Release entries returned: `public-cslib-fmt-finite-graph-diameter-2026-06-02`, `cslib-lbc-1-2026-04-26`, `cslib-fmt-distance-layer-closed-grep-clean-2026-04-23` | Release metadata observed; assets and reproducibility not audited |
| [`darkness-region-dynamics-null-test`](https://github.com/inaciovasquez2020/darkness-region-dynamics-null-test) | No GitHub release entries returned | No release pointer verified in this pass; absence of a release is not itself a defect |
| [`dfm-mkc-cosmology`](https://github.com/inaciovasquez2020/dfm-mkc-cosmology) | Release entries returned: `v1.0.0`, `dfm-mkc-cosmology-post-closure-validation-2026-06-02`, `zenodo-2026-05-26-r2` | Release metadata observed; assets and reproducibility not audited |
| [`fo4-constraint-isolation`](https://github.com/inaciovasquez2020/fo4-constraint-isolation) | No GitHub release entries returned | No release pointer verified in this pass; absence of a release is not itself a defect |
| [`frontier-status-dashboard`](https://github.com/inaciovasquez2020/frontier-status-dashboard) | Release entries returned: `zenodo-2026-05-26-r2`, `zenodo-2026-05-26` | Release metadata observed; assets and reproducibility not audited |
| [`inaciovasquez2020`](https://github.com/inaciovasquez2020/inaciovasquez2020) | No GitHub release entries returned | No release pointer verified in this pass; absence of a release is not itself a defect |
| [`inaciovasquez2020.github.io`](https://github.com/inaciovasquez2020/inaciovasquez2020.github.io) | No GitHub release entries returned | No release pointer verified in this pass; absence of a release is not itself a defect |
| [`poincare-new-derivation`](https://github.com/inaciovasquez2020/poincare-new-derivation) | Release entries returned: `pnd-cdt-1-2026-04-26` | Release metadata observed; assets and reproducibility not audited |
| [`theorem-closure-classifier`](https://github.com/inaciovasquez2020/theorem-closure-classifier) | Release entries returned: `v0.1.3`, `v0.1.2`, `v0.1.1` | Release metadata observed; assets and reproducibility not audited |
| [`urf-11-translation-subproblem-registry`](https://github.com/inaciovasquez2020/urf-11-translation-subproblem-registry) | No GitHub release entries returned | No release pointer verified in this pass; absence of a release is not itself a defect |
| [`urf-core`](https://github.com/inaciovasquez2020/urf-core) | Release entries returned: `urf-core-freeze-2026-02`, `zenodo-2026-05-26`, `v_ack_vardi` | Release metadata observed; assets and reproducibility not audited |
| [`urf-spine-public`](https://github.com/inaciovasquez2020/urf-spine-public) | No GitHub release entries returned | No release pointer verified in this pass; absence of a release is not itself a defect |
| [`urf-templates`](https://github.com/inaciovasquez2020/urf-templates) | Release entries returned: `v0.1.0` | Release metadata observed; assets and reproducibility not audited |
| [`urf-textbook`](https://github.com/inaciovasquez2020/urf-textbook) | Release entries returned: `v0.3.1`, `v0.3.0`, `v0.2.0` | Release metadata observed; assets and reproducibility not audited |
| [`urf-verifier`](https://github.com/inaciovasquez2020/urf-verifier) | Release entries returned: `uv-vbc-1-2026-04-26`, `v1.1.0`, `v1.0.0` | Release metadata observed; assets and reproducibility not audited |
| [`vasquez-index`](https://github.com/inaciovasquez2020/vasquez-index) | Release entries returned: `vi-ibc-1-2026-04-26`, `pca-2026-04-26` | Release metadata observed; assets and reproducibility not audited |
| [`zero_day_restricted_closures`](https://github.com/inaciovasquez2020/zero_day_restricted_closures) | No GitHub release entries returned | No release pointer verified in this pass; absence of a release is not itself a defect |

**Audit result:** release metadata is present for 12 repositories and no release entries were returned for 7. This is a release-pointer inventory, not a quality ranking. A missing release does not mean a repository is invalid; a release entry does not prove that its artifacts reproduce or that its scientific claims are correct. The JSON receipt marks artifact hashes and reproducibility as not audited.
