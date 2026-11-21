"""Canonical paths. Never hardcode artifacts/."""

from __future__ import annotations

import os
from pathlib import Path


def repo_root() -> Path:
    env = os.environ.get("QTL_ROOT")
    if env:
        return Path(env).expanduser().resolve()
    # packages/qtl-core/src/qtl_core/paths.py -> repo root
    return Path(__file__).resolve().parents[4]


def artifacts() -> Path:
    return repo_root() / "artifacts"


def artifact(*parts: str) -> Path:
    path = artifacts().joinpath(*parts)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
