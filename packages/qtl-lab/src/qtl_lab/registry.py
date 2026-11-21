"""Filesystem plugin discovery."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from qtl_core.paths import repo_root

PLUGIN_KINDS = (
    "notebooks",
    "papers",
    "posts",
    "projects",
    "data",
    "datasets",
    "models",
)


@dataclass
class Plugin:
    kind: str
    slug: str
    path: Path
    meta: dict


def _load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return data if isinstance(data, dict) else {}


def discover(kind: str | None = None) -> list[Plugin]:
    root = repo_root()
    kinds = (kind,) if kind else PLUGIN_KINDS
    found: list[Plugin] = []
    for k in kinds:
        base = root / k
        if not base.is_dir():
            continue
        for child in sorted(base.iterdir()):
            if not child.is_dir() or child.name.startswith("_"):
                continue
            meta = _load_yaml(child / "config.yaml")
            if not meta and k == "data":
                meta = _load_yaml(child / "manifest.yaml")
            if not meta and k == "notebooks":
                # notebook folders may only contain .ipynb
                meta = {"name": child.name, "status": "draft"}
            found.append(Plugin(kind=k, slug=child.name, path=child, meta=meta))
    return found
