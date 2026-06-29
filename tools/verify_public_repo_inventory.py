#!/usr/bin/env python3
import json
import os
import pathlib
import sys
import urllib.request

OWNER = os.environ.get("GITHUB_OWNER", "inaciovasquez2020")
ROOT = pathlib.Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "data" / "public_repo_inventory.generated.json"
README = ROOT / "README.md"

def fail(msg: str) -> None:
    print(f"PUBLIC_REPO_INVENTORY_FAIL := {msg}", file=sys.stderr)
    raise SystemExit(1)

def fetch_public_repo_names(owner: str) -> list[str]:
    names = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{owner}/repos?type=public&per_page=100&page={page}"
        req = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "vasquez-public-repo-inventory-verifier",
            },
        )
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
        if not payload:
            break
        names.extend(r["name"] for r in payload if not r.get("private"))
        if len(payload) < 100:
            break
        page += 1
    return sorted(set(names), key=str.lower)

if not INVENTORY.exists():
    fail(f"missing {INVENTORY.relative_to(ROOT)}")
if not README.exists():
    fail("missing README.md")

inventory = json.loads(INVENTORY.read_text())
records = inventory.get("repositories")
if not isinstance(records, list):
    fail("repositories is not a list")

indexed = sorted({r.get("name") for r in records if r.get("name")}, key=str.lower)
visible = fetch_public_repo_names(OWNER)

if len(indexed) != len(visible):
    fail(f"index_count={len(indexed)} github_visible_count={len(visible)}")
if indexed != visible:
    missing = sorted(set(visible) - set(indexed), key=str.lower)
    extra = sorted(set(indexed) - set(visible), key=str.lower)
    fail(f"missing={missing} extra={extra}")

for rec in records:
    for field in ("name", "url", "role", "status", "boundary"):
        if not rec.get(field):
            fail(f"repo={rec.get('name')} missing_field={field}")

readme = README.read_text()
for name in visible:
    if f"[`{name}`]" not in readme and f"| `{name}`" not in readme:
        fail(f"README missing repo row {name}")

if inventory.get("public_repository_count") != len(visible):
    fail(f"metadata_count={inventory.get('public_repository_count')} github_visible_count={len(visible)}")

print("PUBLIC_REPO_INVENTORY_OK")
