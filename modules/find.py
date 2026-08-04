import config as c
import curses
import modules.globals as g
import modules.graphics as gfx

def show_find_screen():

	# Clear screen
	gfx.draw_base_screen(
		"Find",
		bottom_prompt="Leave empty to cancel",
		show_colon=False
	)

	# Show cursor
	curses.curs_set(1)

	curses.echo()

	# Listen for input
	raw_input = g.stdscr.getstr(1, 0, c.MAX_SEARCH_LENGTH)

	curses.noecho()

	curses.curs_set(0)