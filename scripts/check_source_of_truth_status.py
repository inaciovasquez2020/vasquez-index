#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS_DOC = ROOT / "docs/status/SOURCE_OF_TRUTH_2026_04_27.md"
README = ROOT / "README.md"

def main() -> int:
    if not STATUS_DOC.exists():
        print(f"missing status document: {STATUS_DOC.relative_to(ROOT)}")
        return 1
    if not README.exists():
        print("missing README.md")
        return 1

    status_text = STATUS_DOC.read_text(encoding="utf-8", errors="ignore")
    readme_text = README.read_text(encoding="utf-8", errors="ignore")

    required_status = [
        "Status: Documentation / Index Surface",
        "does not independently prove mathematical claims",
        "Any theorem status must inherit from a buildable formal repository",
        "This repository must not claim independent theorem verification.",
    ]

    required_readme = [
        "## Formal Status",
        "Status: Documentation / Index Surface",
        "It does not independently prove mathematical claims.",
        "Every theorem-level claim must inherit from a buildable formal source repository.",
        "`docs/status/SOURCE_OF_TRUTH_2026_04_27.md`",
    ]

    missing = [s for s in required_status if s not in status_text]
    missing += [s for s in required_readme if s not in readme_text]

    if missing:
        print("source-of-truth status check failed")
        for s in missing:
            print(f"missing: {s}")
        return 1

    print({
        "status": "PASS",
        "classification": "Documentation / Index Surface",
        "status_doc": str(STATUS_DOC.relative_to(ROOT)),
        "readme_status_block": "PASS",
    })
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
