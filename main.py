import sys
from app.executor import gui_execute
from app.api_calling import icon_locator
from app.api_calling import icon_click

"""
=== Function Reference for main.py ===

1. gui_execute(command: str) -> None
   - Sends a GUI command to be executed.
   - Example: gui_execute("click:100,200") will click at screen coordinates (100, 200).

2. icon_locator(icon_path: str, mode: str = "exact") -> list[tuple[int, int]]
   - Searches the screen for an icon image and returns a list of (x, y) center coordinates where it appears.
   - Parameters:
       icon_path: Path to the image file (e.g., "icons/save.png")
       mode: Matching method — "exact" for pixel-perfect match, or "scale" for scaled matching.
   - Returns: List of coordinates. Empty list if no match is found.

3. icon_click(icon_path: str, mode: str = "exact") -> tuple[int, int] | None
   - Wraps icon_locator and automatically clicks the first matching icon found.
   - If running on macOS (sys.platform == "darwin"), coordinates are divided by 2 to account for Retina scaling.
   - Returns the (x, y) clicked, or None if the icon is not found.
"""


# Write your main logic below:

pass