#!/usr/bin/env python3
from pathlib import Path

p = Path("docs/status/FORMAL_CONTENT_AUDIT_2026_04_27.md")
if not p.exists():
    raise SystemExit("missing formal content audit registry")

text = p.read_text(encoding="utf-8")

required = [
    "total repositories audited: 54",
    "repositories with Lean source: 23",
    "repositories with no Lean source: 31",
    "`pachner-invariant` | proof-facing",
    "`cslib-fmt` | support-library candidate",
    "`chronos-urf-rr` | conditional flagship",
    "The repository network is a frontier-certification and research-infrastructure portfolio with a small proof-facing Lean surface, not a theorem-complete proof network.",
    "Forbidden descriptions:",
    "machine-checked proof when the core result depends on `axiom`, `admit`, `sorry`, `:= True`, or placeholder witnesses",
]

for needle in required:
    if needle not in text:
        raise SystemExit(f"missing required audit phrase: {needle}")

for forbidden in [
    "the repository network proves the Clay problems",
    "the repository network is theorem-complete",
    "all major conjectures are solved",
]:
    if forbidden in text.lower():
        raise SystemExit(f"forbidden overclaim present: {forbidden}")

print("formal content audit registry: PASS")
