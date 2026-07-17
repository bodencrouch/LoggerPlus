"""Minimal misc helpers vendored for standalone loggerplus."""
from __future__ import annotations

import os
import sys
from pathlib import Path


def ensure_directory_exists(path: Path | str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


def is_debug_mode() -> bool:
    ret = False
    if os.getenv("PYTHONDEBUG", None):
        ret = True
    if getattr(sys, "gettrace", None) is not None:
        ret = True
    if getattr(sys, "frozen", False) or getattr(sys, "_MEIPASS", False):
        ret = False
    if os.getenv("DEBUG_MODE", "0") == "1":
        ret = True
    return ret
