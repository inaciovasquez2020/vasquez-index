# Contributing to Vasquez Index

This repository is the canonical index and navigation hub for the URF repository network.

## Contribution classes

### 1. Documentation improvements

- clarify navigation wording
- improve onboarding text
- improve route descriptions across registry surfaces
- fix broken or ambiguous references

### 2. Registry and verification hardening

- improve repository verification surfaces
- tighten registry-facing checks
- improve reproducibility guidance
- harden status/index consistency

### 3. Scope or canonicality changes

These require explicit justification.

- changing registry role declarations
- changing canonicality language
- changing frozen/status boundaries
- expanding authority claims

## Preferred workflow

```bash
git fetch origin --prune
git switch main
git pull --ff-only origin main
git switch -c your-branch-name
```

Run the repository check before commit:

```bash
make verify
```

Then commit:

```bash
git add <files>
git commit -m "docs: improve onboarding surface"
git push -u origin your-branch-name
```

## Disallowed without explicit justification

- silent semantic changes
- changing canonical authority language without synchronized status updates
- expanding scope or status claims without updating the registry surfaces
