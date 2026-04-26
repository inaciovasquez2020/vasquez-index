Status: Canonical public index / registry surface
Last updated: 2026-04-17

Scope:
- Public-facing index and dashboard surface
- Registry and canonicality layer
- Reference links to canonical repositories and artifacts

Verification:
- make verify
- .github/workflows/verify.yml

## Repository-Scope Closure: VI-IBC-1

Index boundary certificate: CLOSED under finite manifest verification and explicit index non-claim boundary.

Closure artifact: `docs/status/INDEX_BOUNDARY_CERTIFICATE.md`.

Executable checker: `scripts/verify_index_boundary_certificate.py`.

No repository-level claim that index placement implies external validation.

No repository-level claim that listed artifacts are peer-reviewed unless explicitly marked.

No repository-level claim that index completeness equals theorem-level completion.

Remaining frontier: actual external review, independent validation, peer-reviewed publication, or theorem-level strengthening in the indexed repositories.
