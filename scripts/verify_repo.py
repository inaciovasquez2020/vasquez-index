#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

required = [
    "README.md", "STATUS.md", "REGISTRY.md", "CANONICALITY.md",
    "CITATION.cff", "docs/index.md", "artifacts/public-repository-inventory.json",
]
missing = [p for p in required if not Path(p).exists()]
if missing:
    print(json.dumps({"valid": False, "missing": missing}, sort_keys=True))
    sys.exit(1)

readme = Path("README.md").read_text(encoding="utf-8")
index = Path("docs/index.md").read_text(encoding="utf-8")
receipt = json.loads(Path("artifacts/public-repository-inventory.json").read_text(encoding="utf-8"))
begin = "<!-- PUBLIC_REPOSITORY_INVENTORY_BEGIN -->"
end_marker = "<!-- PUBLIC_REPOSITORY_INVENTORY_END -->"
if readme.count(begin) != 1 or readme.count(end_marker) != 1:
    print(json.dumps({"valid": False, "error": "inventory_markers_missing_or_duplicated"}))
    sys.exit(1)
inventory_text = readme.split(begin, 1)[1].split(end_marker, 1)[0]
table_names = re.findall(r"\|\s*\[\x60([^\x60]+)\x60\]\(https://github\.com/inaciovasquez2020/[^)]+\)", inventory_text)
index_names = re.findall(r"https://github\.com/inaciovasquez2020/([A-Za-z0-9_.-]+)", index)
receipt_names = [item["name"] for item in receipt.get("repositories", [])]
checks = {
    "required_files_present": True,
    "inventory_names_unique": len(table_names) == len(set(table_names)),
    "receipt_names_unique": len(receipt_names) == len(set(receipt_names)),
    "inventory_count_matches_receipt": len(table_names) == receipt.get("public_repository_count_observed"),
    "inventory_matches_receipt": set(table_names) == set(receipt_names),
    "navigation_matches_inventory": set(index_names) == set(table_names),
    "all_receipt_entries_public": all(item.get("visibility") == "public" for item in receipt.get("repositories", [])),
    "receipt_count_consistent": receipt.get("account_repository_count_observed") == receipt.get("public_repository_count_observed", 0) + receipt.get("private_repository_count_observed", 0),
    "nonclaim_boundary_present": "public_repository_inventory_implies_theorem_level_closure" in receipt.get("invariant", ""),
}
failed = [key for key, value in checks.items() if not value]
result = {
    "valid": not failed, "checks": checks, "failed_checks": failed,
    "inventory_count": len(table_names), "navigation_count": len(index_names), "receipt_count": len(receipt_names),
    "note": "This verifies inventory/navigation consistency only; it does not audit artifacts or prove scientific claims."
}
print(json.dumps(result, sort_keys=True))
sys.exit(1 if failed else 0)
