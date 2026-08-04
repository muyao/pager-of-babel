import curses
import random
import config as c
import modules.globals as g
import modules.graphics as gfx
import modules.unrandom as unrand

def show_find_screen():

	# Clear screen
	gfx.draw_base_screen(
		"Find",
		bottom_prompt="Leave empty to cancel",
		show_colon=False
	)

	# Show cursor
	curses.curs_set(1)

	# Show written text
	curses.echo()

	# Listen for input
	raw_input = g.stdscr.getstr(1, 0, c.MAX_SEARCH_LENGTH).decode("utf-8")

	# Cancel if raw input is empty
	if raw_input == "":
		return

	# Hide written text
	curses.noecho()

	# Hide cursor
	curses.curs_set(0)

	# Clear screen
	gfx.draw_base_screen(
		"Find",
		bottom_prompt=f"Finding {raw_input}...",
		show_colon=False
	)

	# Sanitise input
	sanitised_input = raw_input
	sanitised_input = sanitised_input.lower()
	sanitised_input = "".join(
		[char for char in sanitised_input if char in c.ALPHABET]
	)

	# Turn input into list of indexes
	sanitised_input = sanitised_input
	sanitised_input_list = []
	for char in sanitised_input:
		sanitised_input_list.append(c.ALPHABET.index(char))

	sanitised_input_list.append(0)
	tmp_range = range(
		int(c.XOR_BIT_LENGTH / 5) - len(sanitised_input_list) - 1
	)
	sanitised_input_list += [
		random.randint(0, len(c.ALPHABET) - 1) for i in tmp_range
	]

	s = 0
	for alpha_idx in sanitised_input_list:
		s <<= 5
		s += alpha_idx

	s <<= 5

	for i in range(c.START_ROLL + 1):
		s = unrand.get_seed(s)

	page = s % c.PAGES_PER_LOG

	log = (s - page) // c.PAGES_PER_LOG

	raise Exception(log, page)