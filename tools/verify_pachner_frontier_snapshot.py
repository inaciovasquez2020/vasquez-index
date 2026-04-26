#!/usr/bin/env python3
from pathlib import Path
text = Path("docs/status/PACHNER_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")
required = [
"Status: Portfolio snapshot",
"inaciovasquez2020/pachner-invariant",
"pachner-certified-frontier-2026-04-26",
"7c41460 docs(pachner): lock certificate value gate and status index",
"Lean build: PASS",
"pytest: 304/304 passed",
"count bridge theorem surface locked",
"2--3 edge-degree chain theorem-level present",
"certificate registry pending descent/topological invariant certificates",
"certificate value gate locked",
"status index locked",
"allEdges_count_eq_edgeDeg_countP",
"allEdges_pachner23_count_delta",
"edgeDeg_pachner23_delta",
"edgeDeg_pachner23_eq_expected",
"No global Pachner descent theorem is asserted.",
"No new topological invariant theorem is asserted.",
"No further Pachner theorem-strengthening step is admissible without descent/topological-invariant certificate input.",
]
forbidden = [
"global Pachner descent theorem is proved",
"topological invariant theorem is proved",
"Pachner invariant is solved",
"Clay problem is solved",
]
missing = [s for s in required if s not in text]
assert not missing, "Missing Pachner frontier snapshot literals:\n" + "\n".join(missing)
assert all(s not in text for s in forbidden), "Forbidden overclaim literal present"
print("Pachner frontier snapshot PASS")
