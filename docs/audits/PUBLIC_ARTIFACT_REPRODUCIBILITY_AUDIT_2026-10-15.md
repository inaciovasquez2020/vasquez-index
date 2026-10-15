# Public Artifact/Reproducibility Evidence Audit

**Observed:** 2026-10-15  
**Scope:** 19 public repositories listed in `artifacts/public-repository-inventory.json`  
**Method:** Static README/source inspection and indexed code search. No local clean clone, build, test suite, release download, or independent hash recomputation was performed.

## Findings: hash and checksum evidence

| Repository | Source evidence | Status |
|---|---|---|
| `urf-core` | `CHECKSUMS.txt`, `transparency/files.sha256`, `scripts/verify_checksums.sh` | Manifest and verifier located; verifier not executed. |
| `urf-verifier` | `transparency/files.sha256`, `transparency/merkle.root`, `.github/workflows/lean_and_certs.yml` | CI hash-comparison mechanism located; this audit did not execute the workflow or independently recompute the manifest. README notes a sample certificate/hash payload is not shipped at the described surface. |
| `dfm-mkc-cosmology` | `tools/verify_dfm_mkc_downloaded_public_payload_manifest.py` checks file existence, byte size, SHA-256, and explicit no-evidence boundaries. | Verifier source inspected, not run. Hash validity does not imply schema validation, external payload verification, protocol execution, or scientific evidence. |
| `urf-textbook` | `releases/v0.1.2/README.md` records a PDF SHA-256 and release tag/commit. | Recorded checksum located; asset digest not independently recomputed. Capsule labels itself release metadata, not theorem closure. |
| `biological-friction-framework` | Indexed source contains SHA-256 checks for selected evidence/input paths. | Some hashing mechanisms located; no global release manifest or clean-clone replay established here. |

## Findings: reproducibility and verifier entry points

| Repository | Documented entry point located | What it does not establish in this audit |
|---|---|---|
| `cslib-fmt` | README says to run `lake build`; pinned Lean toolchain is claimed. | Build was not run here; no release-artifact hash independently checked. |
| `fo4-constraint-isolation` | README names `python3 tools/verify_fo4_constraint_isolation.py` and additional canonical verifier paths. | Commands were not executed here. README explicitly limits the package to FO⁴ constraint isolation. |
| `theorem-closure-classifier` | README gives `python -m pytest -q` and `python verifier/run_controls.py`. | Neither command was run here; the expected control count in documentation is not independently confirmed. |
| `urf-11-translation-subproblem-registry` | README names `python3 tools/verify_urf11_registry.py`. | Verifier was not run; registry consistency is not theorem closure. |
| `urf-templates` | README gives a runnable example verifier and test command under `examples/non_urf_scientific_claim_demo/`; it links a clean-clone confirmation note. | Neither the clean-clone path nor commands were executed in this audit; the demo explicitly makes no universal scientific-validation claim. |
| `zero_day_restricted_closures` | README surfaces `python3 verification/anti_unconditional_rule.py`. | Command was not run; the README explicitly denies unrestricted closure claims. |
| `chronos-urf-rr` | README identifies a conditional frontier/executable surface and describes build, artifact-schema, boundary, and verifier checks. | No clean build or test was executed here; README expressly does not claim repository-level theorem closure. |
| `darkness-region-dynamics-null-test` | README defines a conditional null-test schema and synthetic-data/no-claims boundary. | No measured null result or reproducible empirical result is established by the README or this audit. |
| `urf-spine-public` | README describes a minimal verifier and finite certificate example. | Exact verifier execution and release-bundle reproduction were not performed. README says the public mirror omits full reduction scripts and private release bundles. |
| `poincare-new-derivation` | README describes a conditional/not-proven descent program and remaining global closure obligations. | No complete Poincaré proof or clean-clone reproduction is established here. |
| `frontier-status-dashboard` | README documents CI/repository-health and theorem-boundary status signals with a non-closure boundary. | Dashboard health is not a proof of referenced claims; no local build was run in this audit. |
| `inaciovasquez2020` | Profile README routes readers to the index, core, executable reference, and exposition; distinguishes verified, conditional, open, and not-claimed. | This is navigation/status documentation, not an artifact reproduction test. |
| `inaciovasquez2020.github.io` | Website README calls itself a documentation/website surface and says theorem claims must inherit from a formal source. | Website presence or build health does not prove referenced mathematics. |

## Search scope limitation

Searches for `reproducibility SHA256 checksum` returned no indexed matches for several repositories, including `cslib-fmt`, `darkness-region-dynamics-null-test`, `fo4-constraint-isolation`, `frontier-status-dashboard`, `inaciovasquez2020`, `inaciovasquez2020.github.io`, and `poincare-new-derivation`. These negative search results are not proof that files or mechanisms are absent. README inspection then identified documented build or verifier entry points in several of those repositories.

The full 19-repository inventory includes the five hash-evidence repositories above and the 14 repositories in the reproducibility table. This is not an exhaustive tree walk of every repository, branch, release asset, or nested submodule.

## Audit totals

- 5 repositories with static hash/checksum evidence located.
- 14 additional repositories with README-level build, verifier, or explicit documentation-boundary evidence inspected.
- 0 manifest/verifier mechanisms executed as part of this audit.
- 0 release asset hashes independently recomputed.
- 0 clean-clone reproductions completed.

## Reproducibility gate for future status promotion

For each selected release: pin the exact tag and commit; obtain declared release assets; follow the repository's documented environment setup; run its verifier and tests in a clean environment; record exact commands, exit codes, hashes, and outputs; preserve failed or missing inputs as unresolved. None of these checks by itself proves a mathematical theorem or scientific conclusion.
