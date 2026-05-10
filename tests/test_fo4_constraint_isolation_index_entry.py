import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_fo4_index_entry_status():
    artifact = json.loads((ROOT / "artifacts/fo4_constraint_isolation_index_entry.json").read_text())
    assert artifact["repository"] == "inaciovasquez2020/fo4-constraint-isolation"
    assert artifact["status"] == "FO4_CONSTRAINT_ISOLATION_ONLY"
    assert artifact["theorem_closure"] is False

def test_fo4_index_entry_doc_boundary():
    text = (ROOT / "docs/status/FO4_CONSTRAINT_ISOLATION_INDEX_ENTRY_2026_05_10.md").read_text()
    assert "FO4_CONSTRAINT_ISOLATION_ONLY" in text
    assert "does not assert" in text
    assert "Chronos-RR closure" in text
    assert "H4.1/FGL closure" in text
    assert "UniversalFiberEntropyGap theorem closure" in text
    assert "P vs NP" in text
    assert "Clay-problem result" in text
