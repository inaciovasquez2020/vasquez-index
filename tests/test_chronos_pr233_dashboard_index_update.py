from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_chronos_pr233_dashboard_index_update_verifier_passes() -> None:
    subprocess.run(
        [sys.executable, "tools/verify_chronos_pr233_dashboard_index_update.py"],
        cwd=ROOT,
        check=True,
    )
