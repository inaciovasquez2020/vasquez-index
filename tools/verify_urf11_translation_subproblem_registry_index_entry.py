import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/status/URF11_TRANSLATION_SUBPROBLEM_REGISTRY_INDEX_ENTRY_2026_05_10.md"
ARTIFACT = ROOT / "artifacts/index/urf11_translation_subproblem_registry_index_entry_2026_05_10.json"

REQUIRED = [
    "URF11_REGISTRY_ONLY",
    "https://github.com/inaciovasquez2020/urf-11-translation-subproblem-registry",
    "22a8e88",
    "ed3e5b9",
    "No unrestricted Chronos-RR closure.",
    "No H4.1/FGL closure.",
    "No UniversalFiberEntropyGap theorem.",
    "No P vs NP.",
    "No Clay-problem closure.",
    "No unrestricted graph-rigidity theorem.",
    "No unrestricted Cayley-graph rigidity theorem.",
]

def main() -> None:
    doc = DOC.read_text()
    artifact = json.loads(ARTIFACT.read_text())
    combined = doc + "\n" + json.dumps(artifact, sort_keys=True)

    for token in REQUIRED:
        assert token in combined, token

    assert artifact["status"] == "URF11_REGISTRY_ONLY"
    assert artifact["initial_commit"] == "22a8e88"
    assert artifact["source_of_truth_guard_merge"] == "ed3e5b9"

if __name__ == "__main__":
    main()
