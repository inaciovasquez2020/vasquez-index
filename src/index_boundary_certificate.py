from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class IndexBoundaryCertificate:
    theorem_id: str
    status: str
    required_count: int
    present_count: int
    missing: tuple[str, ...]
    all_required_present: bool
    boundary_declared: bool


def _normalize_required(paths: Iterable[str]) -> tuple[str, ...]:
    out: list[str] = []
    for p in paths:
        s = str(p).strip()
        if not s:
            raise ValueError("required paths must be nonempty")
        out.append(s)
    if not out:
        raise ValueError("at least one required path is needed")
    return tuple(out)


def missing_required_paths(root: Path | str, required: Sequence[str]) -> tuple[str, ...]:
    base = Path(root)
    normalized = _normalize_required(required)
    return tuple(p for p in normalized if not (base / p).exists())


def index_boundary_certificate(root: Path | str, required: Sequence[str], boundary_text: str) -> IndexBoundaryCertificate:
    normalized = _normalize_required(required)
    missing = missing_required_paths(root, normalized)
    boundary = str(boundary_text)
    boundary_declared = all(
        token in boundary
        for token in [
            "No repository-level claim that index placement implies external validation.",
            "No repository-level claim that listed artifacts are peer-reviewed unless explicitly marked.",
            "No repository-level claim that index completeness equals theorem-level completion.",
        ]
    )
    passed = not missing and boundary_declared
    return IndexBoundaryCertificate(
        theorem_id="VI-IBC-1",
        status="PASS" if passed else "FAIL",
        required_count=len(normalized),
        present_count=len(normalized) - len(missing),
        missing=missing,
        all_required_present=not missing,
        boundary_declared=boundary_declared,
    )
