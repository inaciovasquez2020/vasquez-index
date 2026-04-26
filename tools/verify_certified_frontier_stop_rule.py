#!/usr/bin/env python3
from pathlib import Path

stop = Path("docs/status/CERTIFIED_FRONTIER_STOP_RULE_2026_04_26.md").read_text(encoding="utf-8")
index = Path("docs/status/CERTIFIED_FRONTIER_INDEX_2026_04_26.md").read_text(encoding="utf-8")
ra1n = Path("docs/status/RA1N_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")
pachner = Path("docs/status/PACHNER_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")
ym = Path("docs/status/YM_OS_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")

required_stop = [
    "Status: Portfolio stop rule",
    "RA1n certified frontier",
    "Pachner certified frontier",
    "Yang--Mills OS certified frontier",
    "docs/status/CERTIFIED_FRONTIER_INDEX_2026_04_26.md",
    "docs/status/RA1N_FRONTIER_SNAPSHOT_2026_04_26.md",
    "docs/status/PACHNER_FRONTIER_SNAPSHOT_2026_04_26.md",
    "docs/status/YM_OS_FRONTIER_SNAPSHOT_2026_04_26.md",
    "No listed frontier may be promoted from certified frontier to theorem closure without new certificate input.",
    "Delta_RA1n > 0",
    "theta/descent closure",
    "global descent gate",
    "nonperturbative OS-positive Euclidean Yang--Mills measure",
    "strictly positive mass gap",
    "No unconditional RA1n theorem is asserted.",
    "No global Pachner descent theorem is asserted.",
    "No new topological invariant theorem is asserted.",
    "No Yang--Mills mass-gap theorem is asserted.",
    "No Clay problem is asserted solved.",
    "No unconditional four-dimensional nonabelian Yang--Mills construction is asserted.",
    "certified frontier surfaces locked",
    "certificate evaluation pending",
    "no final theorem closure asserted",
]

missing = [s for s in required_stop if s not in stop]
if missing:
    raise SystemExit("Missing certified frontier stop-rule literals:\n" + "\n".join(missing))

cross_checks = {
    "index": [
        "RA1n certified frontier",
        "Pachner certified frontier",
        "Yang--Mills OS certified frontier",
        "No Clay problem is claimed solved here.",
    ],
    "ra1n": [
        "ra1n-certified-frontier-2026-04-26",
        "No unconditional RA1n theorem is asserted.",
    ],
    "pachner": [
        "pachner-certified-frontier-2026-04-26",
        "No global Pachner descent theorem is asserted.",
        "No new topological invariant theorem is asserted.",
    ],
    "ym": [
        "ym-os-certified-frontier-2026-04-26",
        "No Yang--Mills mass-gap theorem is asserted.",
        "No Clay problem is asserted solved.",
        "No unconditional four-dimensional nonabelian Yang--Mills construction is asserted.",
    ],
}

sources = {
    "index": index,
    "ra1n": ra1n,
    "pachner": pachner,
    "ym": ym,
}

for name, literals in cross_checks.items():
    text = sources[name]
    for literal in literals:
        if literal not in text:
            raise SystemExit(f"{name} missing required literal: {literal}")

for forbidden in [
    "Clay problem is solved",
    "RA1n is solved unconditionally",
    "global Pachner descent theorem is proved",
    "topological invariant theorem is proved",
    "Yang--Mills mass-gap theorem is proved",
    "unconditional four-dimensional nonabelian Yang--Mills construction is proved",
]:
    if forbidden in index or forbidden in ra1n or forbidden in pachner or forbidden in ym:
        raise SystemExit(f"Forbidden overclaim literal present outside stop-rule list: {forbidden}")

print("Certified frontier stop rule PASS")
