import subprocess
import sys
from pathlib import Path


def test_ra1n_frontier_snapshot_locked() -> None:
    text = Path("docs/status/RA1N_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")
    assert "Status: Portfolio snapshot" in text
    assert "inaciovasquez2020/clay-problem-lab" in text
    assert "ra1n-certified-frontier-2026-04-26" in text
    assert "483/483 tests passed" in text
    assert "unrestricted RA1n admissibility is refuted" in text
    assert "certified nondegenerate RA1n theorem surface is locked" in text
    assert "certificate registry is pending actual values" in text
    assert "No unconditional RA1n theorem is asserted." in text
    assert "No further RA1n theorem-strengthening step is admissible without actual certificate values." in text


def test_ra1n_frontier_snapshot_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "tools/verify_ra1n_frontier_snapshot.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "RA1n frontier snapshot PASS" in result.stdout
