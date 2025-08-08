"""
executor.py
A thin wrapper around PyAutoGUI that executes Yuantsy‑standard GUI action strings.
"""

from __future__ import annotations
import sys
import time
import pyautogui
import pyperclip                   # for type‑by‑clipboard
from typing import Callable, Dict
from app.keymap import to_pyautogui

pyautogui.FAILSAFE = True          # move mouse to top‑left to abort
pyautogui.PAUSE    = 0.05          # small delay after each action


# --------------------------------------------------------------------------- #
#  Dispatcher
# --------------------------------------------------------------------------- #

def _scroll(args: str) -> None:
    x, y = map(int, args.split(","))
    if x:
        pyautogui.hscroll(x)
    if y:
        pyautogui.scroll(y)

def _click(args: str, clicks: int = 1, button: str = "left") -> None:
    x, y = map(int, args.split(","))
    pyautogui.click(x, y, clicks=clicks, button=button)

def _drag(args: str) -> None:
    x1, y1, x2, y2 = map(int, args.split(","))
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, duration=0.2, button="left")

def _press(args: str) -> None:
    pyautogui.press(to_pyautogui(args))

def _type(args: str) -> None:
    pyautogui.typewrite(list(args))

'''
def _hotkey(args: str) -> None:
    keys = [to_pyautogui(k.strip()) for k in args.split(",")]
    pyautogui.hotkey(*keys)
'''

def _hotkey(params: str) -> None:
    """
    Simultaneous hotkey press: press all keys, then release all keys.
    Mimics NutJS-like key chord (not sequential press).
    """
    keys = [to_pyautogui(k.strip()) for k in params.split(",")]

    # Press all keys
    for key in keys:
        pyautogui.keyDown(key)

    # Release all keys (in reverse)
    for key in reversed(keys):
        pyautogui.keyUp(key)


def _type_clip(args: str) -> None:
    pyperclip.copy(args)
    # Cmd on macOS, Ctrl elsewhere
    paste_key = "command" if sys.platform == "darwin" else "ctrl"
    pyautogui.hotkey(paste_key, "v")

def _wait(args: str) -> None:
    ms = int(args)
    time.sleep(ms / 1000)


_ACTIONS: Dict[str, Callable[[str], None]] = {
    "scroll":        _scroll,
    "click":         lambda a: _click(a, 1, "left"),
    "double-click":  lambda a: _click(a, 2, "left"),
    "right-click":   lambda a: _click(a, 1, "right"),
    "drag":          _drag,
    "press":         _press,
    "type":          _type,
    "hotkey":        _hotkey,
    "type-by-clipboard": _type_clip,
    "wait":          _wait,
}


# --------------------------------------------------------------------------- #
#  Public entry‑point
# --------------------------------------------------------------------------- #

def gui_execute(action: str) -> None:
    """
    Execute **one** Yuantsy‑standard action string.

    >>> gui_execute("click:920,1814")
    >>> gui_execute("type:hello world")
    >>> gui_execute("hotkey:ctrl,c")
    """
    try:
        verb, args = action.split(":", 1)
    except ValueError:
        raise ValueError(f"Malformed action: '{action}'")
    func = _ACTIONS.get(verb)
    if func is None:
        raise ValueError(f"Unknown action verb '{verb}'")
    func(args)
