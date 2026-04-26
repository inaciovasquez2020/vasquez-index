import subprocess
import sys
from pathlib import Path


def test_pachner_frontier_snapshot_locked() -> None:
    text = Path("docs/status/PACHNER_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")
    assert "Status: Portfolio snapshot" in text
    assert "inaciovasquez2020/pachner-invariant" in text
    assert "pachner-certified-frontier-2026-04-26" in text
    assert "7c41460 docs(pachner): lock certificate value gate and status index" in text
    assert "Lean build: PASS" in text
    assert "pytest: 304/304 passed" in text
    assert "count bridge theorem surface locked" in text
    assert "2--3 edge-degree chain theorem-level present" in text
    assert "certificate registry pending descent/topological invariant certificates" in text
    assert "certificate value gate locked" in text
    assert "status index locked" in text
    assert "No global Pachner descent theorem is asserted." in text
    assert "No new topological invariant theorem is asserted." in text


def test_pachner_frontier_snapshot_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "tools/verify_pachner_frontier_snapshot.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Pachner frontier snapshot PASS" in result.stdout
