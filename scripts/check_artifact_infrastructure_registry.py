from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/status/ARTIFACT_INFRASTRUCTURE_REGISTRY_2026_04_27.md"

required_phrases = [
    "Status: Cross-Repo Artifact Infrastructure Registry",
    "Scope: repository infrastructure only.",
    "does not assert theorem-level completion",
    "does not assert theorem-level completion, external validation, publication acceptance, or mathematical closure",
    "`vasquez-index`",
    "`poincare-new-derivation`",
    "`pachner-invariant`",
    "`clay-problem-lab`",
    "`ym-os-quantization`",
    "`chronos-urf-rr`",
    "`urf-core`",
    "`urf-textbook`",
    "Stop rule",
    "does not upgrade any repository to solved",
]

forbidden_phrases = [
    "all theorem-level claims are complete",
    "repository is externally validated",
    "repositories are externally validated",
    "repository is peer reviewed",
    "repositories are peer reviewed",
    "repository is mathematically closed",
    "repositories are mathematically closed",
    "solves navier-stokes",
    "solves yang-mills",
    "solves poincare",
    "solves p vs np",
]

def main() -> int:
    if not REGISTRY.exists():
        print(f"missing registry: {REGISTRY.relative_to(ROOT)}")
        return 1

    text = REGISTRY.read_text(encoding="utf-8")
    lowered = text.lower()
    failures = []

    for phrase in required_phrases:
        if phrase not in text:
            failures.append(f"missing required phrase: {phrase}")

    for phrase in forbidden_phrases:
        if phrase in lowered:
            failures.append(f"forbidden overclaim phrase present: {phrase}")

    if failures:
        print("ARTIFACT_INFRASTRUCTURE_REGISTRY: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("ARTIFACT_INFRASTRUCTURE_REGISTRY: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
