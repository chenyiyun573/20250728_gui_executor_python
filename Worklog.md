
To install:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir icons
```

To use:
Put the icons that you need to locate into the folder named icons.
Then write your own main logic in main.py to run it. 


20250728 1946 PT
the hotkey like gui_execute("cmd","space") does not work. 
changed the code to:
```
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
```


20250728 2008 PT
The hotkey(cmd,N) for pyautogui to execute is functioning like Shift+Command+N on Macbook keyboard. 
We should type like hotkey(cmd,n) if we only want Command+N.


20250808 1608 PT
Move other things into package app, and add a wrap of icon_locator named icon_click to directly click icon position.

