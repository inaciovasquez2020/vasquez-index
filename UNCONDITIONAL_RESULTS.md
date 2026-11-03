# Scoped Results and Proof Availability

**Status date:** 2026-11-02  
**Document class:** Public research-status inventory; not a proof artifact or a claim of originality.

This page records exact mathematical statements supported by inspected source files, while distinguishing public proof sources from private-only evidence. **A theorem proved for objects satisfying its formal hypotheses does not establish that those hypotheses hold for every object in a larger conjecture.** The repository containing this index does not itself prove any result listed below.

## Evidence levels used here

- **Public Lean source:** The cited source file contains the stated Lean declaration and a proof term/tactic script. Readers can inspect it. The index does **not** claim that it independently rebuilt the full dependency closure or audited every imported axiom.
- **Private Lean source:** The source declaration was inspected with repository access, but public readers cannot reproduce the proof from this page. No private code, commit identifier, certificate, or path is released here.
- **Private mathematical exposition:** A written derivation exists, but this index does not classify it as a machine-checked proof or independently reviewed publication.
- **Open:** An essential global extension is not established by the cited sources.

## Public proof sources: precise, scoped statements

| Program | Verified source-level statement | Public evidence | Boundary |
| --- | --- | --- | --- |
| Poincaré triangulation program | For a `CertifiedAscentBarrierStep K L` (a certified legal `2→3, 3→2, 3→2` sequence from a closed triangulation core), `PhiSupport L + 4 = PhiSupport K`. The same source proves strict endpoint descent, well-foundedness of this macro-step relation, and geometric-carrier homeomorphism for an actual certified step. | [`AscentBarrierInvariant.lean`](https://github.com/inaciovasquez2020/poincare-new-derivation/blob/main/lean/Poincare/AscentBarrierInvariant.lean) | **Not** an existence theorem for such a step from every positive-defect triangulation; `JIID` and global stabilized descent remain open. The source explicitly records a counterexample to a narrower proposed universal coverage premise. |
| Finite information, URF core | For `P : FiniteMutualInformationData α β` on finite types, `finiteMutualInformation P ≤ Real.log (Fintype.card α)`. The finite-kernel specialization applies this bound to a jointly constructed distribution. | [`FiniteMutualInformationCardinality.lean`](https://github.com/inaciovasquez2020/urf-core/blob/main/lean/URF/Foundation/FiniteMutualInformationCardinality.lean) · [`FiniteKernelMutualInformationBound.lean`](https://github.com/inaciovasquez2020/urf-core/blob/main/lean/URF/Foundation/FiniteKernelMutualInformationBound.lean) | A finite Shannon-information bound, not a complexity-class separation or a universal URF theorem. |
| Quotient linear algebra | If submodules `K` and `S` satisfy `K ⊓ S = ⊥`, the canonical linear map `K → M ⧸ S` is injective. | [`QuotientLinear.lean`](https://github.com/inaciovasquez2020/biological-friction-framework/blob/main/BiologicalFriction/QuotientLinear.lean) | Standard scoped linear-algebra fact; no biological treatment, efficacy, or novel mechanism follows. |

The public sources above were inspected as text. **This inventory did not independently run Lean or establish axiom-clean transitive dependencies.** Verification or novelty claims should be strengthened only after that separate audit.

## Private-only evidence: descriptive status, not public reproducibility

| Program | Scoped evidence inspected | Access / verification status | Boundary |
| --- | --- | --- | --- |
| Pachner theta | A private Lean counterexample defines a `Valid23Exact` move with `theta` equal to **1085 before** and **1104 after**; its theorem refutes unrestricted nonincrease under that repository's `Valid23Exact` definition. | **Private Lean source; public independent replay unavailable.** No code or finite input fixture is published here. | The formal predicate does not include a manifold/link condition. This does not disprove any suitably strengthened manifold-specific descent assertion. |
| BEpTy profile | Private Lean source proves invariance of finite-radius rooted-ball profile counts under graph isomorphism, and a radius-one incidence-star count equality when the relevant incidence-degree multisets agree. | **Private Lean source; public independent replay unavailable.** | No general profile preservation follows for an unspecified or incidence-forgetting BEpTy normalizer. |
| Damped linear oscillator, WS-EFIS-1 and WS-BV-2 | Under `m,c,k>0`, an integrable forcing `f ∈ L¹([0,∞))`, and a finite set of positive impulse times or strictly increasing positive impulse times tending to infinity with `∑ⱼ |pⱼ| < ∞`, the right-continuous solution satisfies `√E(t) ≤ √E(0) + (∫₀∞ |f(s)| ds + ∑ⱼ |pⱼ|)/√(2m)` for `t ≥ 0`, and `(x(t),v(t)) → (0,0)` as `t → ∞`. This is the WS-BV-2 extension of the finite-impulse energy argument in WS-EFIS-1. | **Private analytic proof; internal second-derivation mathematical audit recorded; merged PR #6; CI reported passing before and after merge. Not Lean-formalized; no unaffiliated referee.** Source and commit details are withheld from this public status page. | Finite-total-variation forcing is sufficient within this linear model; no assertion for arbitrary forcing or nonlinear dynamics, no empirical engineering certification, and no complexity-class separation. |

These descriptions reveal only theorem scope and evidence class. They do not publish private implementation material or elevate a private check to a public certificate.

## Open global bridges (not promoted)

- **Poincaré:** No universal existence proof of a certified stabilized descending path for every relevant positive-defect triangulation; global fan/reentry rigidity and `JIID` remain unresolved.
- **P versus NP:** No verified uniform separating lower bound establishing the conjecture.
- **Yang–Mills / Riemann hypothesis:** Local analytic or algebraic results do not establish the required global conclusions.
- **BEpTy / Chronos:** A valid graph realization and preservation/reduction bridge is still required before broad rigidity statements can be claimed.

## Gate for a future sanitized public certificate

**First candidate:** the finite Pachner-theta counterexample, because its statement has explicit before/after numerical witnesses and a narrowly specified formal validity predicate. **Release status: NOT READY / NOT PUBLISHED.**

**Independent review request:** [GitHub issue #57](https://github.com/inaciovasquez2020/vasquez-index/issues/57). The standalone candidate has been locally replayed with SHA-256 `e53b942535e6d08b02770a6382f82116289afeaffd3f9a699e3272661f82ffda`, but **no unaffiliated reproduction has been received**. The candidate archive is not publicly published. Before publication:

1. Reproduce the exact finite witness and `Valid23Exact` definition in a new, standalone public-safe artifact without copying protected private data or repository history.
2. Check that every required definition, license, provenance statement, and dependency is safe to disclose.
3. Independently execute the certificate or a minimal Lean checker against the frozen artifact; record commands, toolchain, exit status, and a SHA-256 digest.
4. State prominently that the witness is **not** asserted to satisfy closed-manifold/link hypotheses.
5. Link the released artifact here only after these conditions pass.

## Interpretation

**Unconditional within stated hypotheses** must not be confused with **unconditional resolution of a major problem**. Public source availability, successful CI, formal compilation, independent reproduction, independent mathematical review, and originality are distinct statuses.

For portfolio-wide governance see [External Status Lock](docs/status/EXTERNAL_STATUS_LOCK.md) and [Lean Proof Portfolio Classification](docs/status/LEAN_PROOF_PORTFOLIO_CLASSIFICATION.md).
