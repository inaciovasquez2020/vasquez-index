#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STATUS_DOC = ROOT / "docs/status/VASQUEZ_INDEX_CHRONOS_PR233_DASHBOARD_UPDATE_2026_05_12.md"
ARTIFACT = ROOT / "artifacts/status/chronos_pr233_dashboard_index_update_2026_05_12.json"

REQUIRED_FILES = [
    ROOT / "README.md",
    STATUS_DOC,
    ARTIFACT,
]

REQUIRED_TOKENS = [
    "chronos-urf-rr",
    "frontier-status-dashboard",
    "PR #231",
    "PR #232",
    "PR #233",
    "PR #50",
    "Repository integrity: 100%",
    "Theorem closure: 82%",
    "Current real Chronos-admissible unrestricted Reg-SNF",
    "Selected DepthBridge reachability",
    "no UniversalFiberEntropyGap closure",
    "no DepthBridge beyond selected final carrier domain",
    "no Chronos-RR theorem-level closure",
    "no H4.1/FGL theorem-level closure",
    "no P vs NP closure",
    "no Clay-problem closure",
]

FORBIDDEN_TOKENS = [
    "UniversalFiberEntropyGap is proved",
    "DepthBridge beyond selected final carrier domain is proved",
    "Chronos-RR theorem-level closure is proved",
    "H4.1/FGL theorem-level closure is proved",
    "P vs NP is proved",
    "Clay-problem closure is proved",
]


def fail(message: str) -> None:
    print(f"verification failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path}")
    return path.read_text()


def main() -> None:
    for path in REQUIRED_FILES:
        if not path.exists():
            fail(f"missing required file: {path}")

    combined = "\n".join(
        read(path)
        for path in [ROOT / "README.md", STATUS_DOC]
        if path.exists()
    )

    for token in REQUIRED_TOKENS:
        if token not in combined:
            fail(f"missing required token: {token}")

    for token in FORBIDDEN_TOKENS:
        if token in combined:
            fail(f"forbidden overclaim token present: {token}")

    artifact = json.loads(read(ARTIFACT))

    if artifact.get("status") != "INDEX_UPDATED / DASHBOARD_SYNCED / FRONTIER_BOUNDARY_PRESERVED":
        fail("artifact status mismatch")

    if artifact.get("theorem_level_closure") is not False:
        fail("artifact must keep theorem_level_closure false")

    percentages = artifact.get("dashboard_percentages", {})
    if percentages.get("repository_integrity") != 100:
        fail("repository_integrity must be 100")
    if percentages.get("theorem_closure") != 82:
        fail("theorem_closure must be 82")

    boundary = set(artifact.get("boundary", []))
    for token in [
        "no UniversalFiberEntropyGap closure",
        "no DepthBridge beyond selected final carrier domain",
        "no Chronos-RR theorem-level closure",
        "no H4.1/FGL theorem-level closure",
        "no P vs NP closure",
        "no Clay-problem closure",
    ]:
        if token not in boundary:
            fail(f"artifact boundary missing: {token}")

    print("Chronos PR233 dashboard index update verified.")


if __name__ == "__main__":
    main()
