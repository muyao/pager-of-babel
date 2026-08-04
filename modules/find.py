import base62
import curses
import random
import config as c
import modules.globals as g
import modules.graphics as gfx
import modules.pages as pg
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

	# Find
	found_location = find(raw_input)

	display_found(found_location)

def find(raw_input):

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

	# Fill chunk with random characters
	# Start with a space so that phrase is separated
	sanitised_input_list.append(0)
	tmp_range = range(
		int(c.XOR_BIT_LENGTH / 5) - len(sanitised_input_list) - 1
	)
	sanitised_input_list += [
		random.randint(0, len(c.ALPHABET) - 1) for i in tmp_range
	]

	# Turn list into state (state of wanted)
	s = 0
	for alpha_idx in sanitised_input_list:
		s <<= 5
		s += alpha_idx
	s <<= 5

	# Find seed of wanted
	for i in range(c.START_ROLL + 1):
		s = unrand.get_seed(s)

	# Turn seed into page, entry and log
	page = s % c.PAGES_PER_ENTRY
	s = (s - page) // c.PAGES_PER_ENTRY
	entry = s % c.ENTRIES_PER_LOG
	s = (s - entry) // c.ENTRIES_PER_LOG
	log = s# % c.LOGS_PER_NEXT_HIERARCHY

	return log, entry, page

def display_found(found_location):

	log, entry, page = found_location

	# In case log name is too long
	log = base62.encode(log)
	if len(log) > c.MAX_LOG_DISPLAY_LENGTH:
		log = f"{log[:7]}..."

	# Clear screen
	gfx.draw_base_screen(
		"Find",
		upper_bottom_prompt=f"Found at log {log}, entry {hex(entry)}, page {page}",
		bottom_prompt="Press enter to go to that location. Press any other key to cancel"
	)

	# Move cursor to after the ':'
	g.stdscr.move(g.MAX_Y - 1, 1)
	
	# Show cursor
	curses.curs_set(1)

	# Listen for user input
	key = g.stdscr.getch()
	if key != ord('\n'):
		return

	pg.current_log, pg.current_entry, pg.current_page = found_location