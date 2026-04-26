import subprocess
import sys
from pathlib import Path


def test_certified_frontier_index_locked() -> None:
    text = Path("docs/status/CERTIFIED_FRONTIER_INDEX_2026_04_26.md").read_text(encoding="utf-8")
    assert "Status: Portfolio frontier index" in text
    assert "RA1n certified frontier" in text
    assert "Pachner certified frontier" in text
    assert "Yang--Mills OS certified frontier" in text
    assert "ra1n-certified-frontier-2026-04-26" in text
    assert "pachner-certified-frontier-2026-04-26" in text
    assert "ym-os-certified-frontier-2026-04-26" in text
    assert "unrestricted RA1n admissibility refuted" in text
    assert "count bridge theorem surface locked" in text
    assert "OS certificate registry locked" in text
    assert "certificate value gate locked" in text
    assert "No Clay problem is claimed solved here." in text
    assert "No unconditional RA1n theorem is claimed." in text
    assert "No global Pachner descent theorem is claimed." in text
    assert "No Yang--Mills mass-gap theorem is claimed." in text


def test_certified_frontier_index_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "tools/verify_certified_frontier_index.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Certified frontier index PASS" in result.stdout
