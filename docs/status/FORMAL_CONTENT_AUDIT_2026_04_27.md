# Formal Content Audit Registry

Date: 2026-04-27

Status: **Portfolio classification lock**

## Purpose

This registry separates repository roles by formal mathematical content.

It prevents documentation, dashboards, axioms, admits, `sorry`, placeholder witnesses, or CI success from being represented as theorem-level closure.

## Audit basis

A static Lean-content audit over the public repository network found:

- total repositories audited: 54
- repositories with Lean source: 23
- repositories with no Lean source: 31
- strongest proof-facing repository: `pachner-invariant`
- strongest support-library candidate: `cslib-fmt`
- best conditional flagship: `chronos-urf-rr`

## Proof-facing repositories

These may be presented as formal proof artifacts, subject to their own stated limits.

| Repository | Status | Boundary |
|---|---|---|
| `pachner-invariant` | proof-facing | Cleanest Lean surface: no axioms, no `sorry`, no `admit`, no `:= True` marker in the audit. The full Pachner theorem layer remains open unless proved in-repo. |
| `cslib-fmt` | support-library candidate | Clean Lean scaffold/support library. Modest theorem scope; not a major theorem proof. |

## Conditional frontier repositories

These may be presented as conditional reductions, certified frontiers, or executable obstruction maps.

| Repository | Status | Boundary |
|---|---|---|
| `chronos-urf-rr` | conditional flagship | Large mixed Lean/repository artifact. Conditional/frontier only; no unconditional complexity lower bound claim. |
| `clay-problem-lab` | conditional experimental lab | Clay-adjacent frontier laboratory. No Millennium theorem closure. |
| `ym-os-quantization` | conditional frontier | Yang--Mills OS frontier/reduction artifact. No OS-positive measure or mass-gap construction claim. |
| `yang-mills-hs-gap-cert` | conditional certificate surface | Certificate-style artifact; analytic content remains conditional where axiomatized. |
| `final-wall-fo-k-locality` | conditional frontier | FO^k locality/frontier artifact; no theorem-complete final wall claim. |
| `capacity-locality-certification` | certification infrastructure | Certification surface only. |

## Infrastructure / exposition repositories

These record, render, verify, index, or explain claims. They are not theorem-proof repositories.

| Repository | Status |
|---|---|
| `vasquez-index` | portfolio index |
| `urf-core` | framework terminology and dependency layer |
| `urf-textbook` | exposition |
| `scientific-infrastructure` | reproducibility infrastructure |
| `urf-verifier` | verifier infrastructure |
| `vasquez-docs` | documentation |

## Legacy / scaffold / quarantine repositories

Repositories with heavy use of axioms, admits, `sorry`, theorem stubs, witness strings, or no Lean source must be treated as scaffold, legacy, or documentation unless individually repaired.

This includes theorem-claim surfaces around:

- Poincare;
- Riemann Hypothesis;
- P vs NP;
- Yang--Mills;
- Hodge;
- BSD;
- Collatz;
- Goldbach;
- twin primes;
- ABC;
- generic `*-formal`;
- generic `*-witness`;
- generic dashboard, archive, and ledger repositories.

## Public rule

Allowed descriptions:

- proof-facing artifact;
- support library;
- conditional frontier;
- certified obstruction map;
- executable audit infrastructure;
- exposition;
- legacy scaffold.

Forbidden descriptions:

- solved Clay problem;
- theorem-complete proof;
- machine-checked proof when the core result depends on `axiom`, `admit`, `sorry`, `:= True`, or placeholder witnesses;
- external validation not actually received.

## Canonical public sentence

The repository network is a frontier-certification and research-infrastructure portfolio with a small proof-facing Lean surface, not a theorem-complete proof network.
