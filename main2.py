from executor import gui_execute

def run_system_command_sequence():
    steps = [
        "hotkey:cmd,space",
        "type:Terminal",
        "wait:1000",
        "press:enter",
        "wait:1000",
        "hotkey:cmd,n",
        "wait:1000",
        "type:curl -o ~/Desktop/code_list.py http://public2.yuantsy.com/Script/20250706_code_list.py",
        "wait:8000",
        "press:enter",
        "wait:4000",
        "type-by-clipboard:cd ~/Desktop",
        "press:enter",
        "type-by-clipboard:python3 ~/Desktop/code_list.py ~/Desktop/gui_executor_python",
        "press:enter",
    ]

    for action in steps:
        try:
            gui_execute(action)
            print(action)
        except Exception as e:
            print(f"[ERROR] Failed to execute: {action} → {e}")

if __name__ == "__main__":
    run_system_command_sequence()

