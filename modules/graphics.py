import curses
import modules.globals as g

def draw_base_screen(info, bottom_prompt="", show_colon=True):
	# Clear screen
	g.stdscr.clear()

	# Title
	title = f"The Pager of Babel - {info}"
	g.stdscr.addstr(0, int((g.MAX_X - len(title)) / 2), title)

	# Bottom prompt
	g.stdscr.addstr(g.MAX_Y - 2, 0, bottom_prompt)

	# The ':' in the bottom left
	if show_colon:
		g.stdscr.addstr(g.MAX_Y - 1, 0, ':')