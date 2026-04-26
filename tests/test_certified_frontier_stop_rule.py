import subprocess
import sys
from pathlib import Path


def test_certified_frontier_stop_rule_locked() -> None:
    text = Path("docs/status/CERTIFIED_FRONTIER_STOP_RULE_2026_04_26.md").read_text(encoding="utf-8")
    assert "Status: Portfolio stop rule" in text
    assert "RA1n certified frontier" in text
    assert "Pachner certified frontier" in text
    assert "Yang--Mills OS certified frontier" in text
    assert "No listed frontier may be promoted from certified frontier to theorem closure without new certificate input." in text
    assert "Delta_RA1n > 0" in text
    assert "theta/descent closure" in text
    assert "nonperturbative OS-positive Euclidean Yang--Mills measure" in text
    assert "No unconditional RA1n theorem is asserted." in text
    assert "No global Pachner descent theorem is asserted." in text
    assert "No Yang--Mills mass-gap theorem is asserted." in text
    assert "no final theorem closure asserted" in text


def test_certified_frontier_stop_rule_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "tools/verify_certified_frontier_stop_rule.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Certified frontier stop rule PASS" in result.stdout
