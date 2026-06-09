from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/status/VASQUEZ_INDEX_PROGRAM_WHOLE_SYNC_2026_06_09.md"
ART = ROOT / "artifacts/status/vasquez_index_program_whole_sync_2026_06_09.json"
VERIFY = ROOT / "tools/verify_vasquez_index_program_whole_sync.py"

def test_vasquez_index_program_whole_sync_artifact():
    data = json.loads(ART.read_text())
    assert data["status"] == "VASQUEZ_INDEX_PROGRAM_WHOLE_SYNC_ONLY"
    assert data["role"] == "public_index_and_navigation_surface"
    assert len(data["program_synced_repositories"]) == 7
    assert "P_vs_NP" in data["claims_not_made"]
    assert "Clay_problem_closure" in data["claims_not_made"]
    assert data["next_admissible_object"] == "Stop"

def test_vasquez_index_program_whole_sync_doc():
    text = DOC.read_text()
    assert "VASQUEZ_INDEX_PROGRAM_WHOLE_SYNC_ONLY" in text
    assert "repository_native_bounded_status_certificate" in text
    assert "concreteAnalyticPackageNextBuildStopLockCertificate" in text
    assert "CSLIB_FMT_BOUNDED_FRONTIER_SYNC_2026_06_09" in text
    assert "THEOREM_CLOSURE_CLASSIFIER_CHAT_PROGRESS_2026_06_09" in text
    assert "Claims not made" in text

def test_vasquez_index_program_whole_sync_verifier():
    result = subprocess.run(
        [sys.executable, str(VERIFY)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "VASQUEZ_INDEX_PROGRAM_WHOLE_SYNC_OK" in result.stdout
