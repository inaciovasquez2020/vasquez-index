#!/usr/bin/env bash
set -euo pipefail

echo "== trust verify =="

if ls tools/verify_*.py >/dev/null 2>&1; then
  for f in tools/verify_*.py; do
    echo "running $f"
    python3 "$f"
  done
fi

if [ -d tests ]; then
  if command -v pytest >/dev/null 2>&1; then
    python3 -m pytest -q
  else
    echo "pytest not installed; skipping pytest"
  fi
fi

if [ -f package.json ]; then
  if command -v npm >/dev/null 2>&1; then
    npm test -- --run || npm test
    npm run build
  else
    echo "npm not installed; skipping npm checks"
  fi
fi

if [ -f lakefile.lean ] || [ -f lakefile.toml ]; then
  if command -v lake >/dev/null 2>&1; then
    lake build
  else
    echo "lake not installed; skipping Lean build"
  fi
fi

if find . -path "./.lake" -prune -o -name "*.lean" -print | grep -q .; then
  echo "Lean audit counts:"
  echo "sorry count:"
  find . -path "./.lake" -prune -o -name "*.lean" -print0 | xargs -0 grep -nE '\bsorry\b' || true
  echo "admit count:"
  find . -path "./.lake" -prune -o -name "*.lean" -print0 | xargs -0 grep -nE '\badmit\b' || true
  echo "axiom count:"
  find . -path "./.lake" -prune -o -name "*.lean" -print0 | xargs -0 grep -nE '\baxiom\b' || true
fi

echo "trust verify complete"
