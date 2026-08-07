import curses
import config as c
import modules.helpers as h

# Global variables
stdscr = None
header_win = None
title_win = None
info_win = None
babel_win = None
footer_win = None
is_running = None
is_in_help_manual = None

# Here actually give them a value
def init(s: curses.window) -> None:

	# Screen
	global stdscr
	stdscr = s

	# Screen height width
	scr_max_y, scr_max_x = stdscr.getmaxyx()

	# Subwindows
	global header_win
	header_win = stdscr.subwin(2, scr_max_x, 0, 0)

	global title_win
	title_win = header_win.subwin(2, h.true_len(c.TITLE), 0, 0)

	global info_win
	info_win = header_win.subwin(
		2,
		scr_max_x - h.true_len(c.TITLE) - 1,
		0,
		h.true_len(c.TITLE) + 1
	)

	global babel_win
	babel_win = stdscr.subwin(scr_max_y - 3, scr_max_x, 2, 0)

	global footer_win
	footer_win = stdscr.subwin(1, scr_max_x, scr_max_y - 1, 0)

	# Is vars
	global is_running
	is_running = True

	global is_in_help_manual
	is_in_help_manual = False