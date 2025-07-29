from executor import gui_execute
from api_calling import icon_locator


# Write your main logic below:
# on mac to use pyautogui to execute mouse actions, the coordinate need to be divided by 2. 
# x, y = int(x / 2), int(y / 2) # with this, when using pyautogui on mac, no need for windows. 



# 1) Find icon on screen
centres = icon_locator("icons/icon.png", mode="exact")
if centres:
    x, y = centres[0]
    x, y = int(x / 2), int(y / 2) # with this, when using pyautogui on mac, no need for windows. 
    gui_execute(f"click:{x},{y}")
    print(f"click:{x},{y}")

    gui_execute("type:hello world")
    print("type:hello world")
    #gui_execute("hotkey:ctrl,c")
else:
    print("Icon not found")
