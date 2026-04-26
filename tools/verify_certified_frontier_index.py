#!/usr/bin/env python3
from pathlib import Path

index = Path("docs/status/CERTIFIED_FRONTIER_INDEX_2026_04_26.md").read_text(encoding="utf-8")
ra1n = Path("docs/status/RA1N_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")
pachner = Path("docs/status/PACHNER_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")
ym = Path("docs/status/YM_OS_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")

required_index = [
    "Status: Portfolio frontier index",
    "RA1n certified frontier",
    "Pachner certified frontier",
    "Yang--Mills OS certified frontier",
    "ra1n-certified-frontier-2026-04-26",
    "pachner-certified-frontier-2026-04-26",
    "ym-os-certified-frontier-2026-04-26",
    "docs/status/RA1N_FRONTIER_SNAPSHOT_2026_04_26.md",
    "docs/status/PACHNER_FRONTIER_SNAPSHOT_2026_04_26.md",
    "docs/status/YM_OS_FRONTIER_SNAPSHOT_2026_04_26.md",
    "unrestricted RA1n admissibility refuted",
    "certified nondegenerate theorem surface locked",
    "margin registry pending actual certificate values",
    "count bridge theorem surface locked",
    "2--3 edge-degree chain theorem-level present",
    "certificate value gate locked",
    "status index locked",
    "OS certificate registry locked",
    "mass-gap / Clay-level claims blocked pending OS-measure certificates",
    "certificate evaluation pending",
    "nonperturbative OS-positive Euclidean Yang--Mills measure",
    "strictly positive mass gap",
    "No Clay problem is claimed solved here.",
    "No unconditional RA1n theorem is claimed.",
    "No global Pachner descent theorem is claimed.",
    "No new topological invariant theorem is claimed.",
    "No Yang--Mills mass-gap theorem is claimed.",
    "No unconditional four-dimensional nonabelian Yang--Mills construction is claimed.",
]

missing = [s for s in required_index if s not in index]
if missing:
    raise SystemExit("Missing certified frontier index literals:\n" + "\n".join(missing))

required_ra1n = [
    "ra1n-certified-frontier-2026-04-26",
    "No unconditional RA1n theorem is asserted.",
]

required_pachner = [
    "pachner-certified-frontier-2026-04-26",
    "No global Pachner descent theorem is asserted.",
    "No new topological invariant theorem is asserted.",
]

required_ym = [
    "ym-os-certified-frontier-2026-04-26",
    "No Yang--Mills mass-gap theorem is asserted.",
    "No Clay problem is asserted solved.",
    "No unconditional four-dimensional nonabelian Yang--Mills construction is asserted.",
]

for s in required_ra1n:
    if s not in ra1n:
        raise SystemExit(f"RA1n snapshot missing required literal: {s}")

for s in required_pachner:
    if s not in pachner:
        raise SystemExit(f"Pachner snapshot missing required literal: {s}")

for s in required_ym:
    if s not in ym:
        raise SystemExit(f"Yang-Mills OS snapshot missing required literal: {s}")

for forbidden in [
    "Clay problem is solved",
    "RA1n is solved unconditionally",
    "global Pachner descent theorem is proved",
    "topological invariant theorem is proved",
    "Yang--Mills mass-gap theorem is proved",
    "unconditional four-dimensional nonabelian Yang--Mills construction is proved",
]:
    if forbidden in index:
        raise SystemExit(f"Forbidden overclaim literal present: {forbidden}")

print("Certified frontier index PASS")
