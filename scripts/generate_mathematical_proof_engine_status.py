from pathlib import Path
import re
import subprocess
from datetime import date

HOME = Path.home()

REPOS = [
    "pachner-invariant",
    "urf-core",
    "chronos-urf-rr",
    "ym-os-quantization",
    "clay-problem-lab",
    "poincare-new-derivation",
    "phase-transition-pnp",
    "urf-axioms",
    "rank-dichotomy-cat0",
    "cslib-fmt",
]

OUT = Path("docs/status/MATHEMATICAL_PROOF_ENGINE_STATUS_2026_05_01.md")

DECL_RE = re.compile(r"^\s*(theorem|lemma)\s+[A-Za-z0-9_'.]+", re.M)
SORRY_RE = re.compile(r"\bsorry\b")
ADMIT_RE = re.compile(r"\badmit\b")
AXIOM_RE = re.compile(r"^\s*axiom\s+[A-Za-z0-9_'.]+", re.M)

def sh(cmd, cwd):
    try:
        p = subprocess.run(
            cmd,
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=180,
        )
        return p.returncode, p.stdout[-2000:]
    except Exception as e:
        return 124, str(e)

rows = []
totals = {
    "lean_files": 0,
    "decls": 0,
    "sorry": 0,
    "admit": 0,
    "axiom": 0,
    "lake_repos": 0,
    "lake_pass": 0,
}

for repo in REPOS:
    root = HOME / repo
    if not root.exists():
        rows.append((repo, "missing", 0, 0, 0, 0, 0, "not checked"))
        continue

    lean_files = [
        p for p in root.rglob("*.lean")
        if ".lake" not in p.parts
        and ".git" not in p.parts
        and "lake-packages" not in p.parts
        and "build" not in p.parts
    ]

    text = ""
    for p in lean_files:
        try:
            text += "\n" + p.read_text(errors="ignore")
        except Exception:
            pass

    decls = len(DECL_RE.findall(text))
    sorry = len(SORRY_RE.findall(text))
    admit = len(ADMIT_RE.findall(text))
    axiom = len(AXIOM_RE.findall(text))

    lake_status = "no lakefile"
    if (root / "lakefile.lean").exists() or (root / "lakefile.toml").exists():
        totals["lake_repos"] += 1
        code, _ = sh(["lake", "build"], root)
        lake_status = "PASS" if code == 0 else "FAIL"
        if code == 0:
            totals["lake_pass"] += 1

    totals["lean_files"] += len(lean_files)
    totals["decls"] += decls
    totals["sorry"] += sorry
    totals["admit"] += admit
    totals["axiom"] += axiom

    rows.append((repo, "present", len(lean_files), decls, sorry, admit, axiom, lake_status))

hole_total = totals["sorry"] + totals["admit"] + totals["axiom"]

if totals["decls"] == 0:
    formal_ratio = 0.0
else:
    formal_ratio = max(0.0, 1.0 - min(1.0, hole_total / max(1, totals["decls"])))

build_ratio = totals["lake_pass"] / totals["lake_repos"] if totals["lake_repos"] else 0.0

proof_engine_score = round(100 * (0.55 * formal_ratio + 0.25 * build_ratio + 0.20 * min(1.0, totals["decls"] / 250)), 1)

md = []
md.append("# Mathematical Proof Engine Status — 2026-05-01")
md.append("")
md.append("Conditional.")
md.append("")
md.append(f"- Estimated proof-engine score: **{proof_engine_score}%**")
md.append(f"- Lean files audited: **{totals['lean_files']}**")
md.append(f"- theorem/lemma declarations: **{totals['decls']}**")
md.append(f"- sorry count: **{totals['sorry']}**")
md.append(f"- admit count: **{totals['admit']}**")
md.append(f"- axiom count: **{totals['axiom']}**")
md.append(f"- lake build pass rate: **{totals['lake_pass']}/{totals['lake_repos']}**")
md.append("")
md.append("Build success is an integrity signal only. It is not theorem-level closure.")
md.append("")
md.append("| Repo | Status | Lean files | theorem/lemma decls | sorry | admit | axiom | lake build |")
md.append("|---|---:|---:|---:|---:|---:|---:|---:|")
for r in rows:
    md.append("| " + " | ".join(map(str, r)) + " |")
md.append("")
md.append("## Promotion target")
md.append("")
md.append("To promote the program as a mathematical proof engine, reduce the highest-value local proof holes before adding new repositories, artifacts, layers, or status documents.")
md.append("")
md.append("Priority order:")
md.append("")
md.append("1. Replace local `sorry` terms with proved lemmas.")
md.append("2. Replace local `admit` terms with explicit named frontier lemmas.")
md.append("3. Quarantine or eliminate non-foundational `axiom` declarations.")
md.append("4. Preserve green `lake build` status across proof-facing repositories.")
md.append("5. Convert isolated finite-instance certificates into reusable Lean lemmas.")
md.append("")
md.append("No unconditional Clay, P≠NP, Yang–Mills, Navier–Stokes, RH, or Hodge theorem is asserted.")
md.append("")

OUT.write_text("\n".join(md))
print(OUT)
