#!/usr/bin/env python3
from pathlib import Path

manifest = Path("docs/status/CERTIFIED_FRONTIER_RELEASE_MANIFEST_2026_04_26.md").read_text(encoding="utf-8")
index = Path("docs/status/CERTIFIED_FRONTIER_INDEX_2026_04_26.md").read_text(encoding="utf-8")
stop = Path("docs/status/CERTIFIED_FRONTIER_STOP_RULE_2026_04_26.md").read_text(encoding="utf-8")
ra1n = Path("docs/status/RA1N_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")
pachner = Path("docs/status/PACHNER_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")
ym = Path("docs/status/YM_OS_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")

required_manifest = [
    "Status: Release manifest",
    "certified-frontier-release-2026-04-26",
    "RA1n certified frontier",
    "Pachner certified frontier",
    "Yang--Mills OS certified frontier",
    "docs/status/CERTIFIED_FRONTIER_INDEX_2026_04_26.md",
    "docs/status/CERTIFIED_FRONTIER_STOP_RULE_2026_04_26.md",
    "docs/status/RA1N_FRONTIER_SNAPSHOT_2026_04_26.md",
    "docs/status/PACHNER_FRONTIER_SNAPSHOT_2026_04_26.md",
    "docs/status/YM_OS_FRONTIER_SNAPSHOT_2026_04_26.md",
    "ra1n-certified-frontier-2026-04-26",
    "pachner-certified-frontier-2026-04-26",
    "ym-os-certified-frontier-2026-04-26",
    "Certified frontier index PASS",
    "Certified frontier stop rule PASS",
    "RA1n frontier snapshot PASS",
    "Pachner frontier snapshot PASS",
    "Yang-Mills OS frontier snapshot PASS",
    "certified frontier surfaces locked",
    "certificate evaluation pending",
    "no final theorem closure asserted",
    "No Clay problem is claimed solved here.",
    "No unconditional RA1n theorem is claimed.",
    "No global Pachner descent theorem is claimed.",
    "No new topological invariant theorem is claimed.",
    "No Yang--Mills mass-gap theorem is claimed.",
    "No unconditional four-dimensional nonabelian Yang--Mills construction is claimed.",
    "No theorem-strengthening step is admissible for any listed frontier without new certificate input.",
]

missing = [s for s in required_manifest if s not in manifest]
if missing:
    raise SystemExit("Missing certified frontier release-manifest literals:\n" + "\n".join(missing))

cross_checks = {
    "index": (index, ["RA1n certified frontier", "Pachner certified frontier", "Yang--Mills OS certified frontier"]),
    "stop": (stop, ["Status: Portfolio stop rule", "No listed frontier may be promoted from certified frontier to theorem closure without new certificate input."]),
    "ra1n": (ra1n, ["ra1n-certified-frontier-2026-04-26", "No unconditional RA1n theorem is asserted."]),
    "pachner": (pachner, ["pachner-certified-frontier-2026-04-26", "No global Pachner descent theorem is asserted."]),
    "ym": (ym, ["ym-os-certified-frontier-2026-04-26", "No Yang--Mills mass-gap theorem is asserted."]),
}

for name, pair in cross_checks.items():
    text, literals = pair
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
    if forbidden in manifest:
        raise SystemExit(f"Forbidden overclaim literal present: {forbidden}")

print("Certified frontier release manifest PASS")
