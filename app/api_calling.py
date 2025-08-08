"""
api_calling.py
Simple client for the icon‑locator service running at http://function.yuantsy.com:8000
"""

from __future__ import annotations
import os
import tempfile
import requests
from typing import List, Tuple
import mss                     # cross‑platform screenshot
from PIL import Image

_BASE_URL = "http://function.yuantsy.com:8000"

def _capture_screen() -> str:
    """Grab a full screen shot, save to tmp PNG, return path."""
    with mss.mss() as sct:
        monitor = sct.monitors[0]
        img = Image.frombytes("RGB", sct.grab(monitor).size, sct.grab(monitor).rgb)
        path = tempfile.mktemp(suffix=".png")
        img.save(path)
        return path

def _call(endpoint: str, screenshot: str, icon: str) -> List[Tuple[int, int]]:
    url = f"{_BASE_URL}{endpoint}"
    with open(screenshot, "rb") as shot, open(icon, "rb") as ico:
        files = {
            "screenshot": ("screenshot.png", shot, "image/png"),
            "icon":       ("icon.png", ico,       "image/png"),
        }
        resp = requests.post(url, files=files, timeout=30)
    resp.raise_for_status()
    return [tuple(pt) for pt in resp.json().get("centres", [])]

# --------------------------------------------------------------------------- #
#  Public helper
# --------------------------------------------------------------------------- #

def icon_locator(icon_path: str = "icon.png",
                 mode: str = "exact",
                 screenshot_path: str | None = None) -> List[Tuple[int, int]]:
    """
    Find icon centres on screen.

    mode ∈ {"exact", "scale"}
    Returns list of (x, y) tuples. Empty → not found.
    """
    if mode not in ("exact", "scale"):
        raise ValueError("mode must be 'exact' or 'scale'")
    if screenshot_path is None:
        screenshot_path = _capture_screen()
    endpoint = "/match/exact" if mode == "exact" else "/match/scale"
    return _call(endpoint, screenshot_path, icon_path)


import sys  # ensure this is imported at the top of api_calling.py

def icon_click(icon_path: str = "icon.png", mode: str = "exact") -> tuple[int, int] | None:
    """
    Locate `icon_path` using `icon_locator` and click the first match.

    - mode: "exact" or "scale" (passed through to icon_locator)
    - On macOS (sys.platform == 'darwin'), the coordinates are halved to
      account for Retina scaling before clicking.

    Returns:
        (x, y) of the position clicked, or None if the icon is not found.
    """
    centres = icon_locator(icon_path=icon_path, mode=mode)
    if not centres:
        return None

    x, y = centres[0]
    if sys.platform == "darwin":
        x, y = int(x / 2), int(y / 2)

    # Prefer the project’s executor so clicks go through the same action path
    from executor import gui_execute
    gui_execute(f"click:{x},{y}")
    return (x, y)
