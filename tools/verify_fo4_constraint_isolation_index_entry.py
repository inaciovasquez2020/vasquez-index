#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

doc = (ROOT / "docs/status/FO4_CONSTRAINT_ISOLATION_INDEX_ENTRY_2026_05_10.md").read_text()
artifact = json.loads((ROOT / "artifacts/fo4_constraint_isolation_index_entry.json").read_text())

assert artifact["repository"] == "inaciovasquez2020/fo4-constraint-isolation"
assert artifact["url"] == "https://github.com/inaciovasquez2020/fo4-constraint-isolation"
assert artifact["status"] == "FO4_CONSTRAINT_ISOLATION_ONLY"
assert artifact["theorem_closure"] is False

required = [
    "FO4_CONSTRAINT_ISOLATION_ONLY",
    "https://github.com/inaciovasquez2020/fo4-constraint-isolation",
    "Canonical public package isolating the FO^4 variable-budget constraint surface",
    "does not assert",
    "Chronos-RR closure",
    "H4.1/FGL closure",
    "UniversalFiberEntropyGap theorem closure",
    "P vs NP",
    "Clay-problem result",
]

for token in required:
    assert token in doc, token

for forbidden in [
    "Chronos-RR is solved",
    "H4.1/FGL is solved",
    "UniversalFiberEntropyGap is proved",
    "P vs NP is solved",
    "Clay problem is solved",
    "unrestricted graph-rigidity theorem is proved",
]:
    assert forbidden not in doc
    assert forbidden not in json.dumps(artifact)

print("FO4 constraint-isolation index entry verified.")
