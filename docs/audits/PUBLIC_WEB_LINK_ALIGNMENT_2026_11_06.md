# Public web navigation alignment audit — 2026-11-06

## Scope and epistemic boundary

GitHub repository inventory inspected for authenticated owner `inaciovasquez2020`: **72 visible repositories**, of which **21 public** and **51 private**. A default-branch root `README.md` fetch was attempted for each; 71 were readable, while one repository did not expose a root README through that route. GitHub code search was additionally used to locate cross-portfolio links and website navigation. The public entry-point HTML, CSS, dashboard source and status-lock workflow surfaces were inspected in more detail.

This is an **inventory-level and targeted web-surface audit**, not an exhaustive traversal of every file, historical commit, external domain or deployed website. No claim about complete link health is made. Private repository names and contents are intentionally omitted from this public report.

## Canonical navigation scheme

| Purpose | Canonical route |
|---|---|
| Public research home | https://inaciovasquez2020.github.io/ |
| Interactive research listing | https://inaciovasquez2020.github.io/#projects |
| Verification explanation | https://inaciovasquez2020.github.io/#method |
| Public publications | https://inaciovasquez2020.github.io/publications.html |
| Contact | https://inaciovasquez2020.github.io/contact.html |
| Repository registry | https://github.com/inaciovasquez2020/vasquez-index |
| Frontier status dashboard source | https://github.com/inaciovasquez2020/frontier-status-dashboard |
| GitHub research profile | https://github.com/inaciovasquez2020 |
| Formal verification boundary | https://inaciovasquez2020.github.io/docs/FORMAL_VERIFICATION_BOUNDARY.html |

Source-of-truth rule: a navigation link or dashboard badge does not replace a theorem declaration, source revision, explicit assumptions, test receipt or independent mathematical review.

## Discrepancies and draft-only corrections

1. Main GitHub Pages website: separate homepage, publications, contact and nested index styling. Harmonized in [draft PR #11](https://github.com/inaciovasquez2020/inaciovasquez2020.github.io/pull/11); regression checks run through `verify`.
2. Vasquez Index: independent style/UX and `publications.html` referenced nonexistent `../styles.css`. Corrected through `portal.css` in [draft PR #59](https://github.com/inaciovasquez2020/vasquez-index/pull/59).
3. Public pages linked to private GitHub repositories. Index pages now preserve names without exposing broken public hyperlinks; no private materials are released.
4. Profile front door lacked a coherent visual navigation strip and its README omitted an expected formal-status block. Addressed in [draft PR #14](https://github.com/inaciovasquez2020/inaciovasquez2020/pull/14).
5. Status dashboard's `/urf-front-door/` path routed back to itself under its Vercel rewrite. Canonical homepage link is in [draft PR #218](https://github.com/inaciovasquez2020/frontier-status-dashboard/pull/218).

All four references are draft branches; their CI and review readiness are independent, and none is authorization to merge or deploy.

## Public repository enumeration

- [`biological-friction-framework`](https://github.com/inaciovasquez2020/biological-friction-framework)
- [`chronos-curated-release`](https://github.com/inaciovasquez2020/chronos-curated-release)
- [`chronos-urf-rr`](https://github.com/inaciovasquez2020/chronos-urf-rr)
- [`cslib-fmt`](https://github.com/inaciovasquez2020/cslib-fmt)
- [`darkness-region-dynamics-null-test`](https://github.com/inaciovasquez2020/darkness-region-dynamics-null-test)
- [`dfm-mkc-cosmology`](https://github.com/inaciovasquez2020/dfm-mkc-cosmology)
- [`fo4-constraint-isolation`](https://github.com/inaciovasquez2020/fo4-constraint-isolation)
- [`frontier-status-dashboard`](https://github.com/inaciovasquez2020/frontier-status-dashboard)
- [`inaciovasquez2020`](https://github.com/inaciovasquez2020/inaciovasquez2020)
- [`inaciovasquez2020.github.io`](https://github.com/inaciovasquez2020/inaciovasquez2020.github.io)
- [`overlap-rigidity-oracle-release`](https://github.com/inaciovasquez2020/overlap-rigidity-oracle-release)
- [`poincare-new-derivation`](https://github.com/inaciovasquez2020/poincare-new-derivation)
- [`theorem-closure-classifier`](https://github.com/inaciovasquez2020/theorem-closure-classifier)
- [`urf-11-translation-subproblem-registry`](https://github.com/inaciovasquez2020/urf-11-translation-subproblem-registry)
- [`urf-core`](https://github.com/inaciovasquez2020/urf-core)
- [`urf-spine-public`](https://github.com/inaciovasquez2020/urf-spine-public)
- [`urf-templates`](https://github.com/inaciovasquez2020/urf-templates)
- [`urf-textbook`](https://github.com/inaciovasquez2020/urf-textbook)
- [`urf-verifier`](https://github.com/inaciovasquez2020/urf-verifier)
- [`vasquez-index`](https://github.com/inaciovasquez2020/vasquez-index)
- [`zero_day_restricted_closures`](https://github.com/inaciovasquez2020/zero_day_restricted_closures)

## Remaining boundaries

- The separate https://www.vasquezresearch.com/ site currently presents standards/certification services rather than the new GitHub Pages research front door. Its source/deployment credentials were not identified from the inspected GitHub repositories. No changes to that external PHP site are claimed.
- The older `scientific-infrastructure` web surface has different styling and links to legacy/private repository names. It is associated with a private source repository; no public source code or private paths are included here.
- Cross-repository historical `README` references, DOI/schema identifiers, archived manuscript URLs, and release snapshots must not be globally rewritten without source-level verification.
- The exact deployed GitHub Pages branch and any custom-domain mapping must be independently confirmed before promotion.
- Actual local Mac repository states and unpushed files have not been inspected.

## Release gate

A public-facing site may be promoted only after CI on exact PR heads, visual mobile/desktop checks, internal/external link audit, status-lock review and explicit user approval. CI success is not mathematical closure.
