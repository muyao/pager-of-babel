import curses
import config as c
import modules.globals as g
import modules.helpers as h

def addstrf(win: curses.window, start_y: int, start_x: int, text: str) -> None:

	# Max y and x
	max_y, max_x = win.getmaxyx()
	# Curr char
	char_idx = 0
	# Attr
	attr = curses.A_NORMAL

	text_iter = iter(text)

	for y in range(max_y):
		for x in range(max_x):

			char = next(text_iter, None)

			# Stop if reached end of text
			if char is None:
				return

			# If char is not the escape char, skip the rest
			if char != c.FANCY_ESCAPE:
				win.addstr(y + start_y, x + start_x, char, attr)
				continue

			# If char is escape char, look at the next char
			char = next(text_iter)

			# If next char is escape char, write escape char itself
			if char == c.FANCY_ESCAPE:
				win.addstr(y + start_y, x + start_x, char, attr)
				continue

			# Otherwise, get the style and draw the next char
			attr = c.FANCY_STYLES[char]

			char = next(text_iter, None)
			# Stop if reached end of text
			if char is None:
				return

			# Write char 2 places after escape char with style (?ab -> b)
			win.addstr(y + start_y, x + start_x, char, attr)

def draw_info(info: str) -> None:
	curses.curs_set(0)
	g.info_win.clear()
	max_y, max_x = g.info_win.getmaxyx()
	addstrf(g.info_win, 0, max_x - h.true_len(info), info)
	g.info_win.refresh()

def draw_on_window(window: curses.window, y: int, x: int, text: str) -> None:
	curses.curs_set(0)
	window.clear()
	addstrf(window, y, x, text)
	window.refresh()