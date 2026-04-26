import subprocess
import sys
from pathlib import Path


def test_certified_frontier_release_manifest_locked() -> None:
    text = Path("docs/status/CERTIFIED_FRONTIER_RELEASE_MANIFEST_2026_04_26.md").read_text(encoding="utf-8")
    assert "Status: Release manifest" in text
    assert "certified-frontier-release-2026-04-26" in text
    assert "RA1n certified frontier" in text
    assert "Pachner certified frontier" in text
    assert "Yang--Mills OS certified frontier" in text
    assert "Certified frontier index PASS" in text
    assert "Certified frontier stop rule PASS" in text
    assert "no final theorem closure asserted" in text
    assert "No Clay problem is claimed solved here." in text
    assert "No Yang--Mills mass-gap theorem is claimed." in text


def test_certified_frontier_release_manifest_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "tools/verify_certified_frontier_release_manifest.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Certified frontier release manifest PASS" in result.stdout
