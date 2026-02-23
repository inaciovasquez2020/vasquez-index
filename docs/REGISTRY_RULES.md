# Vasquez Index — Registry Rules

## Purpose
This repository is a canonical registry of externally versioned,
auditable scientific artifacts. It does not host theory or executable
code; it records authoritative pointers.

## Scope
The index may list repositories, releases, documents, or artifacts that:
- Are publicly accessible
- Have a stable canonical version (tag or release)
- Are intended for long-term citation or audit

## Inclusion Criteria
An entry MUST satisfy all of the following:
1. Canonical version tag exists (e.g. v1.0.0-*-frozen)
2. Repository declares its own scope and invariants
3. Artifact is reproducible or explicitly marked non-executable
4. No unresolved semantic ambiguity at the declared version

## Exclusion Criteria
Entries MUST NOT:
- Point to moving targets (branches without tags)
- Depend on unpublished private artifacts
- Require implicit context not documented at the target

## Versioning Policy
- The index itself is versioned.
- Each index release represents a snapshot of accepted canonical roots.
- Index updates are additive unless an entry is formally deprecated.

## Change Policy
Allowed changes:
- Adding new entries that meet inclusion criteria
- Adding clarifying metadata or links
- Deprecating entries with justification

Disallowed changes:
- Silent replacement of targets
- Retagging or rewriting indexed history
- Removing entries without deprecation notice

## Review Model
- Changes are made via pull request.
- Review checks structural validity only (not scientific correctness).
- Acceptance asserts registry consistency, not claim endorsement.

## Citation
Users SHOULD cite:
- The index version (tag)
- The specific indexed artifact and its tag

The index itself makes no claims beyond registry accuracy.
