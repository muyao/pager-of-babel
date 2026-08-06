import curses
import modules.globals as g
import modules.graphics as gfx
from pathlib import Path

def show_manual() -> None:

	max_y, max_x = g.babel_win.getmaxyx()
	max_y -= 1

	# Info
	gfx.draw_info("Press Enter to exit    ?bHelp Manual?n")
	gfx.draw_on_window(g.footer_win, 0, 0, ':')

	# Read from resources/help.txt
	with open(
		Path(__file__).resolve().parent.parent / "resources" / "help.txt",
		"r"
	) as f:
		help_text = f.readlines()

	line_offset = 0

	g.is_in_help_manual = True
	while g.is_in_help_manual:

		# Clear
		g.babel_win.clear()

		# Write lines
		for line in range(max_y):

			# Stop if reached end of text
			if line + line_offset == len(help_text):
				break

			# Write single line
			gfx.addstrf(
				g.babel_win,
				line,
				0,
				help_text[line + line_offset]
			)

		g.stdscr.move(g.MAX_Y - 1, 1)
		curses.curs_set(1)
		g.babel_win.refresh()

		key = g.stdscr.getch()

		if key == ord(' '):
			line_offset += max_y
		elif key == ord('b'):
			line_offset -= max_y
		elif key == ord('j') or key == curses.KEY_DOWN:
			line_offset += 1
		elif key == ord('k') or key == curses.KEY_UP:
			line_offset -= 1
		elif key == ord('\n'):
			g.is_in_help_manual = False

		if line_offset >= len(help_text):
			line_offset = len(help_text) - 1
		elif line_offset < 0:
			line_offset = 0