import curses
import config as c
import modules.helpers as h

# Global variables
stdscr = None
header_win = None
title_win = None
info_win = None
MAX_X = None
MAX_Y = None
is_running = None

# Here actually give them a value
def init(s: curses.window) -> None:

	# Screen
	global stdscr
	stdscr = s

	# Width and height
	global MAX_Y
	global MAX_X
	MAX_Y, MAX_X = stdscr.getmaxyx()

	# Subwindows
	global header_win
	header_win = stdscr.subwin(2, MAX_X, 0, 0)

	global title_win
	title_win = header_win.subwin(2, h.true_len(c.TITLE), 0, 0)

	global info_win
	info_win = header_win.subwin(2, MAX_X - h.true_len(c.TITLE) - 1, 0, h.true_len(c.TITLE) + 1)

	# Is running
	global is_running
	is_running = False