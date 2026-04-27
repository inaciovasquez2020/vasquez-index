from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/status/ARTIFACT_INFRASTRUCTURE_REGISTRY_2026_04_27.md"

def test_artifact_infrastructure_registry_verifier_passes():
    result = subprocess.run(
        [sys.executable, "scripts/check_artifact_infrastructure_registry.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "ARTIFACT_INFRASTRUCTURE_REGISTRY: PASS" in result.stdout

def test_artifact_infrastructure_registry_has_core_repositories():
    text = REGISTRY.read_text(encoding="utf-8")
    for repo in [
        "`vasquez-index`",
        "`poincare-new-derivation`",
        "`pachner-invariant`",
        "`clay-problem-lab`",
        "`ym-os-quantization`",
        "`chronos-urf-rr`",
        "`urf-core`",
        "`urf-textbook`",
    ]:
        assert repo in text

def test_artifact_infrastructure_registry_preserves_boundaries():
    text = REGISTRY.read_text(encoding="utf-8").lower()
    assert "does not assert theorem-level completion" in text
    assert "does not upgrade any repository to solved" in text
    assert "external validation status" in text
