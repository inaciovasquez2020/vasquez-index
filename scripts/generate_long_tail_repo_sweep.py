#!/usr/bin/env python3
from pathlib import Path
import subprocess

HOME = Path.home()
OUT = Path("docs/status/LONG_TAIL_REPO_SWEEP_2026_04_27.md")

COMPLETED = {
    "cyclone-terminal-obstruction",
    "urf-axioms",
    "urf-core",
    "clay-problem-lab",
    "poincare-new-derivation",
    "biological-friction-framework",
    "chronos-urf-rr",
    "flagship-lean",
    "CorrRank",
    "overlap-rigidity-lean",
    "overlap-rigidity-lean-dev",
    "cslib-fmt",
    "vasquez-index",
    "urf-textbook",
    "inaciovasquez2020.github.io",
    "inaciovasquez2020",
}

STATUS_FILES = {
    "SOURCE_OF_TRUTH_2026_04_27.md",
    "FORMAL_STATUS_2026_04_27.md",
    "CONDITIONAL_FRONTIER_STATUS_2026_04_27.md",
    "CONDITIONAL_STATUS_2026_04_27.md",
    "DEPRECATED_CONDITIONAL_STATUS_2026_04_27.md",
    "SCAFFOLD_STATUS_2026_04_27.md",
    "TRIVIALITY_BOUNDARY_2026_04_27.md",
    "DEFINITIONAL_COLLAPSE_STATUS_2026_04_27.md",
    "THEOREM_SURFACE_AUDIT_2026_04_27.md",
    "OPEN_OBLIGATION_INVENTORY_2026_04_27.md",
    "AXIOM_INVENTORY_2026_04_27.md",
    "ADMIT_INVENTORY_2026_04_27.md",
}

def git_root_name(path: Path) -> str:
    return path.name

def tracked_status_files(repo: Path) -> list[str]:
    status = repo / "docs/status"
    if not status.exists():
        return []
    return sorted(p.name for p in status.glob("*.md") if p.name in STATUS_FILES)

def is_git_repo(path: Path) -> bool:
    return (path / ".git").exists()

repos = sorted(
    [p for p in HOME.iterdir() if p.is_dir() and is_git_repo(p)],
    key=lambda p: p.name.lower(),
)

rows = []
for repo in repos:
    name = git_root_name(repo)
    status_files = tracked_status_files(repo)
    if name in COMPLETED:
        classification = "completed-primary"
    elif status_files:
        classification = "has-status-surface"
    else:
        classification = "needs-sweep"
    rows.append((name, classification, ", ".join(status_files) if status_files else "none"))

needs = [r for r in rows if r[1] == "needs-sweep"]

OUT.write_text(
    "# Long-Tail Repository Sweep — 2026-04-27\n\n"
    "Status: Inventory Only\n\n"
    "This report inventories local Git repositories under `$HOME` and classifies which repositories still need a theorem-status or source-of-truth boundary.\n\n"
    "## Boundary\n\n"
    "This report does not assert theorem verification. It only identifies remaining repositories requiring status normalization.\n\n"
    f"Total local repositories scanned: {len(rows)}\n\n"
    f"Remaining repositories needing sweep: {len(needs)}\n\n"
    "## Repositories needing sweep\n\n"
    + ("\n".join(f"- `{name}`" for name, _, _ in needs) if needs else "- None")
    + "\n\n## Full inventory\n\n"
    "| Repository | Classification | Status files |\n"
    "|---|---|---|\n"
    + "\n".join(f"| `{name}` | {classification} | {files} |" for name, classification, files in rows)
    + "\n",
    encoding="utf-8",
)

print({
    "status": "PASS",
    "total_repositories": len(rows),
    "needs_sweep": len(needs),
    "report": str(OUT),
})
