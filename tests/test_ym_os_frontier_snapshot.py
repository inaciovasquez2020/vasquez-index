import subprocess
import sys
from pathlib import Path


def test_ym_os_frontier_snapshot_locked() -> None:
    text = Path("docs/status/YM_OS_FRONTIER_SNAPSHOT_2026_04_26.md").read_text(encoding="utf-8")
    assert "Status: Portfolio snapshot" in text
    assert "inaciovasquez2020/ym-os-quantization" in text
    assert "ym-os-certified-frontier-2026-04-26" in text
    assert "4b6b828 docs(ym): add OS certificate frontier gate" in text
    assert "Yang-Mills OS certificate registry PASS" in text
    assert "Yang-Mills OS certificate value gate PASS" in text
    assert "Yang-Mills OS status index PASS" in text
    assert "ym-os-quantization: PASS" in text
    assert "certificate verifier: valid" in text
    assert "No Yang--Mills mass-gap theorem is asserted." in text
    assert "No Clay problem is asserted solved." in text
    assert "No unconditional four-dimensional nonabelian Yang--Mills construction is asserted." in text


def test_ym_os_frontier_snapshot_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "tools/verify_ym_os_frontier_snapshot.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Yang-Mills OS frontier snapshot PASS" in result.stdout
