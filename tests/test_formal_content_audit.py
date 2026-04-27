import subprocess
import sys
from pathlib import Path

def test_formal_content_audit_registry_present():
    p = Path("docs/status/FORMAL_CONTENT_AUDIT_2026_04_27.md")
    assert p.exists()
    text = p.read_text(encoding="utf-8")
    assert "proof-facing" in text
    assert "conditional frontier" in text
    assert "legacy scaffold" in text
    assert "not a theorem-complete proof network" in text

def test_formal_content_audit_verifier_passes():
    result = subprocess.run(
        [sys.executable, "scripts/verify_formal_content_audit.py"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    assert result.returncode == 0, result.stdout
