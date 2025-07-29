

# 🖱️ GUI Agent Action Executor & Icon Locator Guide

This guide explains how to use the `gui_execute` and `icon_locator` functions to perform GUI automation with mouse and keyboard actions, along with visual icon detection.

---

## 🔧 Installation

1. Clone the repo and install the Python dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Ensure you have the icon image (e.g. `icon.png`) saved in your working directory.

---

## 🚀 Quick Start

```python
from executor import gui_execute
from api_calling import icon_locator

# Locate an icon visually using screenshot + icon.png
centres = icon_locator("icon.png", mode="exact")

if centres:
    x, y = centres[0]
    gui_execute(f"click:{x},{y}")
    gui_execute("type:hello world")
    gui_execute("hotkey:ctrl,c")
else:
    print("Icon not found.")
```

---

## 🎯 `icon_locator()` — Locate Icon in Screenshot

### Signature

```python
icon_locator(icon_path: str = "icon.png", mode: str = "exact") -> List[Tuple[int, int]]
```

### Description

Detects the position(s) of an icon (e.g., a button or logo) inside a desktop screenshot, and returns a list of center coordinates.

### Parameters

| Param       | Type  | Description                                |
| ----------- | ----- | ------------------------------------------ |
| `icon_path` | `str` | Path to the icon image you want to locate. |
| `mode`      | `str` | `"exact"` or `"scale"` – see below.        |

### Matching Modes

* **`exact`**: Fast. Best if the icon is copy-paste identical. (default)
* **`scale`**: Robust. Useful if the desktop has DPI scaling or the icon was resized.

### Returns

A list of `(x, y)` pixel positions for the centers of all matched icons on screen.

---

## 🧠 `gui_execute()` — Execute an Action String

### Signature

```python
gui_execute(action: str) -> None
```

### Description

Executes one GUI action, using your standard string format (Yuantsy GUI Action Specification).

---

## 🧭 Action String Formats

Use these string formats to represent GUI operations:

### 🖱 Mouse Actions

| Action       | Format             | Example                |
| ------------ | ------------------ | ---------------------- |
| Scroll       | `scroll:x,y`       | `scroll:0,-500`        |
| Single click | `click:x,y`        | `click:100,200`        |
| Double click | `double-click:x,y` | `double-click:400,300` |
| Right click  | `right-click:x,y`  | `right-click:500,400`  |
| Drag         | `drag:x1,y1,x2,y2` | `drag:100,100,200,200` |

### ⌨️ Keyboard Actions

| Action             | Format                       | Example                        |
| ------------------ | ---------------------------- | ------------------------------ |
| Press key          | `press:key`                  | `press:enter`                  |
| Type string        | `type:yourtext`              | `type:hello world`             |
| Hotkey combination | `hotkey:key1,key2,...`       | `hotkey:ctrl,c`                |
| Clipboard typing   | `type-by-clipboard:yourtext` | `type-by-clipboard:long text…` |

### ⏳ Wait

| Action     | Format              | Example             |
| ---------- | ------------------- | ------------------- |
| Delay/wait | `wait:milliseconds` | `wait:3000` (3 sec) |

---

## 🎹 Key Name Specification

Use lowercase strings for keys:

* **Letters & Digits**: `a` to `z`, `0` to `9`
* **Arrows**: `up`, `down`, `left`, `right`
* **Function Keys**: `shift`, `ctrl`, `alt`, `cmd`
* **Special Keys**: `esc`, `space`, `tab`, `enter`, `backspace`
* **Symbols**: `` ` ~ ! @ # $ % ^ & * ( ) - = [ ] ; ' , . / \ ``

🚫 Not supported: `fn`, `f1`\~`f12`, `capslock`, `del`

---

## 🪄 Example Usage

```python
gui_execute("wait:1000")
gui_execute("type:hello world")
gui_execute("hotkey:ctrl,a")
gui_execute("press:backspace")
gui_execute("type-by-clipboard:fast input by clipboard!")
```

---

## 🧪 Testing

You can manually test the action system like this:

```bash
python3
>>> from executor import gui_execute
>>> gui_execute("click:300,500")
>>> gui_execute("type:hi there")
```

---

## 🧷 Notes

* The `icon_locator` API connects to: `http://function.yuantsy.com:8000`
* This system is designed to be modular and OS-aware (Mac vs. Windows key differences are handled internally).
* `pyautogui.FAILSAFE` is **enabled**: moving your mouse to the top-left corner will abort execution.

---

## ✅ Summary

| Task                  | Use this...                             |
| --------------------- | --------------------------------------- |
| Detect icon on screen | `icon_locator("icon.png")`              |
| Click at a coordinate | `gui_execute("click:x,y")`              |
| Send key sequences    | `gui_execute("type:hello")`             |
| Use clipboard typing  | `gui_execute("type-by-clipboard:text")` |
| Chain steps           | Combine `icon_locator` + `gui_execute`  |

You're now ready to automate GUI workflows with visual feedback and full mouse/keyboard scripting!
