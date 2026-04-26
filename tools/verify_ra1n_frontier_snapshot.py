#!/usr/bin/env python3
from pathlib import Path

text = Path("docs/status/RA1N_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")

required = [
    "Status: Portfolio snapshot",
    "inaciovasquez2020/clay-problem-lab",
    "ra1n-certified-frontier-2026-04-26",
    "483/483 tests passed",
    "unrestricted RA1n admissibility is refuted",
    "certified nondegenerate RA1n theorem surface is locked",
    "certificate registry is pending actual values",
    "noncertifying numerical probe is available",
    "No unconditional RA1n theorem is asserted.",
    "\\Delta_{\\mathrm{RA1n}}",
    "No further RA1n theorem-strengthening step is admissible without actual certificate values.",
]

forbidden = [
    "RA1n is solved unconditionally",
    "unconditional RA1n theorem is proved",
    "Navier-Stokes is solved",
    "Clay problem is solved",
]

missing = [s for s in required if s not in text]
assert not missing, "Missing RA1n frontier snapshot literals:\n" + "\n".join(missing)
assert all(s not in text for s in forbidden), "Forbidden overclaim literal present"

print("RA1n frontier snapshot PASS")
