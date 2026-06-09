#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/status/VASQUEZ_INDEX_PROGRAM_WHOLE_SYNC_2026_06_09.md"
ART = ROOT / "artifacts/status/vasquez_index_program_whole_sync_2026_06_09.json"

REQUIRED_REPOS = {
    "urf-core",
    "chronos-urf-rr",
    "urf-textbook",
    "dfm-mkc-cosmology",
    "cslib-fmt",
    "frontier-status-dashboard",
    "theorem-closure-classifier",
}

REQUIRED_NONCLAIMS = {
    "new_theorem_proof",
    "unrestricted_graph_theorem",
    "unrestricted_SLVed_closure",
    "analytic_Einstein_matter_estimate_proof",
    "empirical_cosmology_validation",
    "Lambda_CDM_failure",
    "gravity_closure",
    "Chronos_RR",
    "H4_FGL",
    "P_vs_NP",
    "Clay_problem_closure",
}

def main() -> int:
    data = json.loads(ART.read_text())
    doc = DOC.read_text()

    assert data["status"] == "VASQUEZ_INDEX_PROGRAM_WHOLE_SYNC_ONLY"
    assert data["role"] == "public_index_and_navigation_surface"
    assert data["next_admissible_object"] == "Stop"

    repos = {entry["repo"] for entry in data["program_synced_repositories"]}
    assert REQUIRED_REPOS <= repos

    nonclaims = set(data["claims_not_made"])
    assert REQUIRED_NONCLAIMS <= nonclaims

    assert "VASQUEZ_INDEX_PROGRAM_WHOLE_SYNC_ONLY" in doc
    assert "program-wide bounded-sync pass" in doc
    assert "frontier-status-dashboard" in doc
    assert "theorem-closure-classifier" in doc
    assert "Claims not made" in doc
    assert "P vs NP" in doc
    assert "any Clay-problem closure" in doc

    print("VASQUEZ_INDEX_PROGRAM_WHOLE_SYNC_OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
