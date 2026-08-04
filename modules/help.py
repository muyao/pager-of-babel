import modules.globals as g
from pathlib import Path

def show_manual():
	# Read from resources/help.txt
	with open(
		Path(__file__).resolve().parent.parent / "resources" / "help.txt",
		"r"
	) as f:
		help_text = f.read()

	# Write onto screen
	g.stdscr.addstr(1, 0, help_text)