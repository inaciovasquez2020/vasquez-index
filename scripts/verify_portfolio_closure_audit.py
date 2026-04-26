#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/status/PORTFOLIO_CLOSURE_AUDIT_2026_04_26.md"
DATA = ROOT / "artifacts/audit/portfolio_closure_audit_2026_04_26.json"

REQUIRED_CERTIFICATES = [
    "WS-EFIS-1",
    "PND-CDT-1",
    "URFP0002-RBC-1",
    "URFP0003-RBC-1",
    "URFP0001-RBC-1",
    "UORL-LBC-1",
    "VI-IBC-1",
    "CLC-CBC-1",
    "SI-IBC-1",
    "UV-VBC-1",
    "URFS-SBC-1",
    "CSLIB-LBC-1",
    "FWFK-LBC-1",
    "CLR-CBC-1",
    "TCC-TBC-1",
]

def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)

def main() -> int:
    require(DOC.exists(), "missing audit document")
    require(DATA.exists(), "missing audit json")
    text = DOC.read_text(encoding="utf-8")
    data = json.loads(DATA.read_text(encoding="utf-8"))

    require(data["audit_id"] == "PCA-2026-04-26", "wrong audit id")
    require(data["status"] == "CLOSED", "audit is not closed")
    require(data["repository_count"] == 15, "wrong repository count")
    require(len(data["repositories"]) == 15, "wrong repository list length")

    found = {item["certificate"] for item in data["repositories"]}
    for cert in REQUIRED_CERTIFICATES:
        require(cert in found, f"missing certificate in json: {cert}")
        require(cert in text, f"missing certificate in doc: {cert}")

    boundary = data["boundary"]
    require(boundary["external_validation_claimed"] is False, "external validation overclaimed")
    require(boundary["peer_reviewed_acceptance_claimed"] is False, "peer review overclaimed")
    require(
        boundary["theorem_level_completion_claimed_beyond_finite_certificate_surface"] is False,
        "theorem-level completion overclaimed",
    )
    require(boundary["conditional_frontier_claims_upgraded"] is False, "frontier claims upgraded")

    for literal in [
        "This audit does not claim external validation.",
        "This audit does not claim peer-reviewed acceptance.",
        "This audit does not claim theorem-level completion beyond each repository's stated finite certificate surface.",
        "This audit does not upgrade conditional or frontier mathematical claims.",
        "Pause new closures.",
    ]:
        require(literal in text, f"missing boundary literal: {literal}")

    print(json.dumps({"audit_id": data["audit_id"], "status": "PASS", "repository_count": 15}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
