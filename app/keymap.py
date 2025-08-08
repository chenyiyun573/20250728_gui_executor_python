"""
keymap.py
Maps Yuantsy key names → PyAutoGUI key names (which follow the OS).
"""

import sys

# Shared mapping
_MAPPING = {
    "esc":        "esc",
    "space":      "space",
    "tab":        "tab",
    "enter":      "enter",
    "backspace":  "backspace",
    "up":         "up",
    "down":       "down",
    "left":       "left",
    "right":      "right",
    # Numbers & letters map to themselves
}

# Modifiers diverge on macOS vs others
if sys.platform == "darwin":
    _MAPPING.update({
        "shift": "shift",
        "ctrl":  "ctrl",
        "alt":   "option",
        "cmd":   "command",
    })
else:
    _MAPPING.update({
        "shift": "shift",
        "ctrl":  "ctrl",
        "alt":   "alt",
        "cmd":   "win",
    })

def to_pyautogui(key: str) -> str:
    """Translate Yuantsy key → PyAutoGUI key; returns the original string if unknown."""
    return _MAPPING.get(key, key)
