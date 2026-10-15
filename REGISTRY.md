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
