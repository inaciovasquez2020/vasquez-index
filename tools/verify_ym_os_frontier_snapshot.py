#!/usr/bin/env python3
from pathlib import Path

text = Path("docs/status/YM_OS_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")

required = [
    "Status: Portfolio snapshot",
    "inaciovasquez2020/ym-os-quantization",
    "ym-os-certified-frontier-2026-04-26",
    "4b6b828 docs(ym): add OS certificate frontier gate",
    "Yang-Mills OS certificate registry PASS",
    "Yang-Mills OS certificate value gate PASS",
    "Yang-Mills OS status index PASS",
    "ym-os-quantization: PASS",
    "certificate verifier: valid",
    "OS certificate registry locked",
    "certificate value gate locked",
    "status index locked",
    "mass-gap / Clay-level claims remain blocked pending OS-measure certificates",
    "nonperturbative OS-positive Euclidean Yang--Mills measure",
    "OS reconstruction",
    "strictly positive mass gap",
    "single-observable clustering certificate",
    "No Yang--Mills mass-gap theorem is asserted.",
    "No Clay problem is asserted solved.",
    "No unconditional four-dimensional nonabelian Yang--Mills construction is asserted.",
    "No further Yang--Mills OS theorem-strengthening step is admissible without new OS-measure and mass-gap certificate input.",
]

forbidden = [
    "Yang--Mills mass-gap theorem is proved",
    "Clay problem is solved",
    "unconditional four-dimensional nonabelian Yang--Mills construction is proved",
]

missing = [s for s in required if s not in text]
if missing:
    raise SystemExit("Missing Yang-Mills OS frontier snapshot literals:\n" + "\n".join(missing))

for s in forbidden:
    if s in text:
        raise SystemExit(f"Forbidden overclaim literal present: {s}")

print("Yang-Mills OS frontier snapshot PASS")
