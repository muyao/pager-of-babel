import curses
import config as c
import modules.globals as g

def addstrf(win: curses.window, text: str) -> None:

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
				win.addstr(y, x, char, attr)
				char_idx += 1
				continue

			# If char is escape char, look at the next char
			char_idx += 1
			char = text[char_idx]

			# If next char is escape char, write escape char itself
			if char == c.FANCY_ESCAPE:
				win.addstr(y, x, char, attr)
				char_idx += 1
				continue

			# Otherwise, get the style and draw the next char
			attr = c.FANCY_STYLES[char]
			char_idx += 1
			char = text[char_idx]
			win.addstr(y, x, char, attr)
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