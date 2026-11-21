from __future__ import annotations

from typing import Any


def run(config: dict[str, Any]) -> int:
    print(f"Project: {config.get('name', 'unknown')}")
    return 0
