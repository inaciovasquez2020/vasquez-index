# Vasquez Index — Canonical Registry Dashboard

This repository backs the registry pages at:
* [Main Registry](https://inaciovasquez2020.github.io/vasquez-index/)
* [Dashboard](https://inaciovasquez2020.github.io/vasquez-index/dashboard.html)

## Purpose
To provide a single canonical registry of enabled repositories, stable references, and reproducibility links.

## Canonicality & Governance

This repository operates under the **Canonicality Doctrine** of the Vasquez Research Program.

All structural claims, artifact-backed proofs, and publication statuses are governed by a single authoritative document:

**→ [`CANONICALITY.md`](./CANONICALITY.md)**

### What this means for readers
- All results are **explicitly bounded** and scope-declared.
- “Structurally Closed” refers to **internal logical closure under bounded verification**, not external consensus.
- In the event of any discrepancy, **machine-verifiable artifacts take precedence** over narrative text.

Visitors should consult `CANONICALITY.md` before citing or extending any result.

---
## Local–Global Information Barrier

Formal FO^k structural theorem establishing limits of locality-based inference.

Source:
https://github.com/inaciovasquez2020/final-wall-fo-k-locality/blob/main/docs/local-global-barrier.tex

## Enabled Repositories and DOIs

The following repositories are currently indexed. DOI links resolve to stable versions on Zenodo.

| Repository Handle | DOI Reference |
| :--- | :--- |
| inaciovasquez2020/chronos-urf-rr | [10.5281/zenodo.18403707](https://doi.org/10.5281/zenodo.18403707) |
| inaciovasquez2020/rank-dichotomy-cat0 | [10.5281/zenodo.18450375](https://doi.org/10.5281/zenodo.18450375) |
| inaciovasquez2020/scientific-infrastructure | [10.5281/zenodo.18442204](https://doi.org/10.5281/zenodo.18442204) |
| inaciovasquez2020/support-drift | [10.5281/zenodo.18434555](https://doi.org/10.5281/zenodo.18434555) |
| inaciovasquez2020/urf-axioms | [10.5281/zenodo.18442235](https://doi.org/10.5281/zenodo.18442235) |
| inaciovasquez2020/urf-core | [10.5281/zenodo.18437927](https://doi.org/10.5281/zenodo.18437927) |

---
Suggested order:
1. scientific-infrastructure
2. urf-core
3. urf-spine
4. chronos-urf-rr
5. Application repositories

## Technical Notes
* **Zenodo Integration:** If repositories do not appear in the registry, verify that third-party access is enabled for the Zenodo integration. 
* **Repository Visibility:** Private repositories are not supported; indexed repositories must be public to ensure reproducibility.
* **Status:** This is an index and registry repository. It contains no executable research code.

## Citation
If you use this registry or the indexed materials, please cite as follows:

```bibtex
@manual{Vasquez_Index_2026,
  author = {Vasquez, Inacio F.},
  title  = {Vasquez Index: Canonical Repository Registry and Dashboard},
  year   = {2026},
  url    = {[https://inaciovasquez2020.github.io/vasquez-index/](https://inaciovasquez2020.github.io/vasquez-index/)}
}
