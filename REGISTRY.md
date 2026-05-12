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
- **Status:** Frozen (spec-complete)

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

### urf-prefab-system
- **Repo:** https://github.com/inaciovasquez2020/urf-prefab-system
- **Role:** Canonical prefab definitions
- **Authority:** Structural
- **Scope:** Invariant-preserving prefab bundles
- **Executable:** No (structure-only)
- **Status:** Registry-aligned

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
