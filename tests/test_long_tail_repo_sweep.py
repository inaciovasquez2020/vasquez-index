import subprocess
import sys
from pathlib import Path

def test_long_tail_repo_sweep_report_generates():
    subprocess.run(
        [sys.executable, "scripts/generate_long_tail_repo_sweep.py"],
        check=True,
    )
    text = Path("docs/status/LONG_TAIL_REPO_SWEEP_2026_04_27.md").read_text()
    assert "Status: Inventory Only" in text
    assert "Remaining repositories needing sweep:" in text
    assert "This report does not assert theorem verification." in text
