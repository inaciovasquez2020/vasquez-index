#!/usr/bin/env python3
from pathlib import Path
import json
import sys

required = [
    "README.md",
    "STATUS.md",
    "REGISTRY.md",
    "CANONICALITY.md",
    "CITATION.cff",
]

missing = [p for p in required if not Path(p).exists()]
if missing:
    print({"valid": False, "missing": missing})
    sys.exit(1)

checks = {}

readme = Path("README.md").read_text(errors="ignore").lower()
checks["mentions_vasquez_index"] = ("vasquez-index" in readme) or ("vasquez index" in readme)
checks["mentions_registry"] = "registry" in readme
checks["mentions_dashboard_or_index"] = ("dashboard" in readme) or ("index" in readme)

status = Path("STATUS.md").read_text(errors="ignore").lower()
checks["status_mentions_canonical"] = "canonical" in status or "freeze" in status

reg = Path("REGISTRY.md").read_text(errors="ignore").lower()
checks["registry_mentions_repo_or_framework"] = ("repo" in reg) or ("framework" in reg)

failed = [k for k,v in checks.items() if not v]
if failed:
    print({"valid": False, "failed_checks": failed, "checks": checks})
    sys.exit(1)

print({"valid": True, "checked": required, "checks": checks})
