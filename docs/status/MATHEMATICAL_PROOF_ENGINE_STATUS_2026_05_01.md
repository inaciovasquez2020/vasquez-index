# Mathematical Proof Engine Status — 2026-05-01

Conditional.

- Estimated proof-engine score: **87.4%**
- Lean files audited: **530**
- theorem/lemma declarations: **890**
- sorry count: **67**
- admit count: **14**
- axiom count: **123**
- lake build pass rate: **6/6**

Build success is an integrity signal only. It is not theorem-level closure.

| Repo | Status | Lean files | theorem/lemma decls | sorry | admit | axiom | lake build |
|---|---:|---:|---:|---:|---:|---:|---:|
| pachner-invariant | present | 35 | 220 | 0 | 0 | 0 | PASS |
| urf-core | present | 54 | 64 | 0 | 13 | 42 | PASS |
| chronos-urf-rr | present | 174 | 292 | 1 | 0 | 0 | PASS |
| ym-os-quantization | present | 0 | 0 | 0 | 0 | 0 | no lakefile |
| clay-problem-lab | present | 1 | 4 | 0 | 0 | 2 | no lakefile |
| poincare-new-derivation | present | 107 | 219 | 64 | 0 | 31 | PASS |
| phase-transition-pnp | present | 0 | 0 | 0 | 0 | 0 | no lakefile |
| urf-axioms | present | 42 | 26 | 2 | 1 | 48 | PASS |
| rank-dichotomy-cat0 | present | 0 | 0 | 0 | 0 | 0 | no lakefile |
| cslib-fmt | present | 117 | 65 | 0 | 0 | 0 | PASS |

## Promotion target

To promote the program as a mathematical proof engine, reduce the highest-value local proof holes before adding new repositories, artifacts, layers, or status documents.

Priority order:

1. Replace local `sorry` terms with proved lemmas.
2. Replace local `admit` terms with explicit named frontier lemmas.
3. Quarantine or eliminate non-foundational `axiom` declarations.
4. Preserve green `lake build` status across proof-facing repositories.
5. Convert isolated finite-instance certificates into reusable Lean lemmas.

No unconditional Clay, P≠NP, Yang–Mills, Navier–Stokes, RH, or Hodge theorem is asserted.
