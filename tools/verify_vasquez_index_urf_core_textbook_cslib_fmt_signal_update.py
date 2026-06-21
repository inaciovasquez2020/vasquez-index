#!/usr/bin/env python3
from pathlib import Path
import json

artifact_path = Path("artifacts/vasquez_index/urf_core_textbook_cslib_fmt_signal_index_update_2026_06_21.json")
doc_path = Path("docs/status/VASQUEZ_INDEX_URF_CORE_TEXTBOOK_CSLIB_FMT_SIGNAL_UPDATE_2026_06_21.md")

data = json.loads(artifact_path.read_text())
doc = doc_path.read_text()

assert data["status"] == "VASQUEZ_INDEX_URF_CORE_TEXTBOOK_CSLIB_FMT_SIGNAL_UPDATE_2026_06_21"
assert data["index_effect"] == "cross_repository_status_index_only"
assert len(data["source_updates"]) == 2

core = data["source_updates"][0]
textbook = data["source_updates"][1]

assert core["repo"] == "urf-core"
assert core["commit"] == "857e954"
assert core["pr"] == 474
assert core["status"] == "CSLIB_FMT_FULL_FORMULA_RADIUS_EXTERNAL_STATUS_SIGNAL_OK"
assert core["also_recorded"] == "URF_CORE_FULL_PYTEST_BASELINE_BLOCKERS_OK"

assert textbook["repo"] == "urf-textbook"
assert textbook["commit"] == "d026cfe"
assert textbook["status"] == "URF_CORE_CSLIB_FMT_SIGNAL_TEXTBOOK_SYNC_OK"

assert "index update only" in data["boundary"]
assert "no new theorem" in data["boundary"]
assert "no proof import" in data["boundary"]
assert "no URF-core repair" in data["boundary"]
assert "no CSLIB-FMT repair" in data["boundary"]

assert "Status: `VASQUEZ_INDEX_URF_CORE_TEXTBOOK_CSLIB_FMT_SIGNAL_UPDATE_2026_06_21`" in doc
assert "commit `857e954`" in doc
assert "commit `d026cfe`" in doc
assert "CSLIB_FMT_FULL_FORMULA_RADIUS_EXTERNAL_STATUS_SIGNAL_OK" in doc
assert "URF_CORE_FULL_PYTEST_BASELINE_BLOCKERS_OK" in doc
assert "URF_CORE_CSLIB_FMT_SIGNAL_TEXTBOOK_SYNC_OK" in doc
assert "index update only" in doc

print("VASQUEZ_INDEX_URF_CORE_TEXTBOOK_CSLIB_FMT_SIGNAL_UPDATE_OK")
