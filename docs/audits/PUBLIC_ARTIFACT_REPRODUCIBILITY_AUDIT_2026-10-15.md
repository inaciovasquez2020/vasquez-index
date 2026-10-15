# Public Artifact/Reproducibility Evidence Audit

**Observed:** 2026-10-15  
**Scope:** 19 public repositories listed in `artifacts/public-repository-inventory.json`  
**Method:** Static source inspection and indexed code search. No local clean clone, build, test suite, release download, or independent hash recomputation was performed.

## Findings

| Repository | Source evidence | Status |
|---|---|---|
| `urf-core` | `CHECKSUMS.txt`, `transparency/files.sha256`, `scripts/verify_checksums.sh` | Manifest and verifier located; verifier not executed. |
| `urf-verifier` | `transparency/files.sha256`, `transparency/merkle.root`, `.github/workflows/lean_and_certs.yml` | CI hash-comparison mechanism located; workflow not executed in this audit. README notes that a sample certificate/hash payload is not shipped at the described surface. |
| `dfm-mkc-cosmology` | `tools/verify_dfm_mkc_downloaded_public_payload_manifest.py` checks file existence, byte size, SHA-256, and explicit no-evidence boundaries. | Verifier source inspected, not run. Hash validity does not imply schema validation, external payload verification, protocol execution, or scientific evidence. |
| `urf-textbook` | `releases/v0.1.2/README.md` records a PDF SHA-256 and release tag/commit. | Recorded checksum located; asset digest not independently recomputed. Capsule states this is release metadata, not theorem closure. |
| `biological-friction-framework` | Indexed source contains SHA-256 checks for selected evidence/input paths. | Some hashing mechanisms located; no global release manifest or clean-clone replay established here. |

## Not established

The remaining 14 repositories are **not classified as lacking** hashes or reproducibility instructions. Searches with no result are not proof of absence. Their release assets, manifests, environment pins, and clean-clone commands remain unaudited.

## Audit totals

- 5 repositories with static hash/checksum evidence located.
- 0 manifest/verifier mechanisms executed as part of this audit.
- 0 release asset hashes independently recomputed.
- 0 clean-clone reproductions completed.

## Reproducibility gate for future status promotion

For each selected release: pin the exact tag and commit; obtain declared release assets; follow the repository's documented environment setup; run its verifier and tests in a clean environment; record exact commands, exit codes, hashes, and outputs; preserve failed or missing inputs as unresolved. None of these checks by itself proves a mathematical theorem or scientific conclusion.
