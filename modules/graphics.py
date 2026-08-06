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

	for y in range(max_y):
		for x in range(max_x):

			# Stop if reached end of text
			if char_idx == len(text):
				return

			char = text[char_idx]

			# If char is not the escape char, skip the rest
			if char != c.FANCY_ESCAPE:
				win.addstr(y + start_y, x + start_x, char, attr)
				char_idx += 1
				continue

			# If char is escape char, look at the next char
			char_idx += 1
			char = text[char_idx]

			# If next char is escape char, write escape char itself
			if char == c.FANCY_ESCAPE:
				win.addstr(y + start_y, x + start_x, char, attr)
				char_idx += 1
				continue

			# Otherwise, get the style and draw the next char
			attr = c.FANCY_STYLES[char]
			char_idx += 1
			# Stop if reached end of text
			if char_idx == len(text):
				return
			char = text[char_idx]
			win.addstr(y + start_y, x + start_x, char, attr)
			char_idx += 1

def draw_info(info: str) -> None:
	g.info_win.clear()
	max_y, max_x = g.info_win.getmaxyx()

	addstrf(g.info_win, 0, max_x - h.true_len(info), info)

def draw_title() -> None:
	g.title_win.clear()
	addstrf(g.title_win, 0, 0, c.TITLE)

def draw_footer(footer: str) -> None:
	g.footer_win.clear()
	addstrf(g.footer_win, 0, 0, footer)