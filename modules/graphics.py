import base62
import curses
import config as c
import modules.globals as g
import modules.helpers as h
import modules.pages as pg

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

def draw_base_screen(
	info: str,
	bottom_prompt: str="",
	upper_bottom_prompt: str="",
	show_colon: bool=True
) -> None:
	# Clear screen
	g.stdscr.clear()

	# Title
	title = f"The Pager of Babel - {info}"
	g.stdscr.addstr(0, int((g.MAX_X - len(title)) / 2), title)

	# Upper bottom prompt
	g.stdscr.addstr(g.MAX_Y - 3, 0, upper_bottom_prompt)

	# Bottom prompt
	g.stdscr.addstr(g.MAX_Y - 2, 0, bottom_prompt)

	# The ':' in the bottom left
	if show_colon:
		g.stdscr.addstr(g.MAX_Y - 1, 0, ':')

def draw_info() -> None:
	g.info_win.clear()
	max_y, max_x = g.info_win.getmaxyx()

	log_str = base62.encode(pg.current_log)
	log_str = h.cut_off_end(log_str, c.MAX_LOG_DISPLAY_LENGTH)

	entry_str = hex(pg.current_entry)

	string = c.INFO_MSG(log_str, entry_str, pg.current_page)

	addstrf(g.info_win, 0, max_x - h.true_len(string), string)

def draw_title() -> None:
	g.title_win.clear()
	addstrf(g.title_win, 0, 0, c.TITLE)