# Setup Guide

This guide is for contributors who want a reliable local environment for Vasquez Index.

## Prerequisites

```bash
python3 --version
git --version
```

Recommended baseline:

- Python 3.10 or newer
- Git
- POSIX shell environment

## Clone

```bash
git clone https://github.com/inaciovasquez2020/vasquez-index.git
cd vasquez-index
```

## Optional virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
```

## Verification

```bash
make verify
```

## Recommended edit loop

```bash
git pull --ff-only origin main
make verify
git status --short
```

## Related files

- `QUICKSTART.md`
- `CONTRIBUTING.md`
- `REGISTRY.md`
- `STATUS.md`
- `CANONICALITY.md`
- `FREEZE.md`
