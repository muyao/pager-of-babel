import modules.globals as g
import modules.graphics as gfx
from pathlib import Path

def show_manual():
	# Hide cursor
	g.cursor_visible = 0

	# Clear screen
	gfx.draw_base_screen(
		"Help Manual",
		bottom_prompt="Press any key to exit help manual",
		show_colon=False
	)

	# Read from resources/help.txt
	with open(
		Path(__file__).resolve().parent.parent / "resources" / "help.txt",
		"r"
	) as f:
		help_text = f.read()

	# Write onto screen
	g.stdscr.addstr(1, 0, help_text)

	# Wait until another key is pressed
	g.stdscr.getch()

	# Show cursor
	g.cursor_visible = 1