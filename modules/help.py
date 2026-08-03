import curses
import modules.globals as g
from pathlib import Path

def show_manual():
	# Read from resources/help.txt
	with open(
		Path(__file__).resolve().parent.parent / "resources" / "help.txt",
		"r"
	) as f:
		help_text = f.readlines()

	for idx, line in enumerate(help_text):
		g.stdscr.addstr(idx + 1, 0, line.replace("\n", ""))

	g.stdscr.refresh()