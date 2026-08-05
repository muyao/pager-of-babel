import base62
import curses
import random
from curses.textpad import Textbox
import config as c
import modules.globals as g
import modules.graphics as gfx
import modules.helpers as h
import modules.pages as pg
import modules.random as rand

def show_find_screen() -> None:

	# Clear screen
	gfx.draw_base_screen(
		"Find",
		bottom_prompt="Leave empty to cancel",
		show_colon=False
	)

	# Show cursor
	curses.curs_set(1)

	# Create subwindow
	win = g.stdscr.subwin(g.MAX_Y - 4, g.MAX_X, 2, 0)

	# Wrap the window in a Textbox box manager
	box = Textbox(win, insert_mode=True)

	# Allow user to edit
	box.edit(h.terminate_check)

	# Get text result
	raw_input = box.gather().strip().replace("_", " ")

	# Limit input to MAX_SEARCH_LENGTH
	if len(raw_input) > c.MAX_SEARCH_LENGTH:
		raw_input = raw_input[:c.MAX_SEARCH_LENGTH]

	# Cancel if raw input is empty
	if raw_input == "":
		return

	# Hide cursor
	curses.curs_set(0)

	# Find
	found_location = find(raw_input)

	display_found(found_location)

def find(raw_input: str) -> tuple[int, int, int]:

	# Clear screen
	gfx.draw_base_screen(
		"Find",
		bottom_prompt=f"Finding {raw_input[:(min(40, len(raw_input)))]}...",
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
	sanitised_input = [c.ALPHABET.index(char) for char in sanitised_input]

	# Fill chunk with random characters
	sanitised_input += [
		random.randint(0, len(c.ALPHABET) - 1) for i in range(
			int(c.RAND_OUT_BIT_LENGTH / c.ALPHABET_BITS) - len(sanitised_input)
		)
	]

	# Turn list into state (state of wanted)
	s = 0
	for alpha_idx in sanitised_input:
		s <<= c.ALPHABET_BITS
		s += alpha_idx

	# Find seed
	s = rand.unrandom(s)

	# Turn seed into page, entry and log
	page = s % c.PAGES_PER_ENTRY
	s = (s - page) // c.PAGES_PER_ENTRY
	entry = s % c.ENTRIES_PER_LOG
	s = (s - entry) // c.ENTRIES_PER_LOG
	log = s# % c.LOGS_PER_NEXT_HIERARCHY

	return log, entry, page

def display_found(found_location: tuple[int, int, int]) -> None:

	log, entry, page = found_location

	# In case log name is too long
	log = base62.encode(log)
	log = h.cut_off_end(log, c.MAX_LOG_DISPLAY_LENGTH)

	# Clear screen
	gfx.draw_base_screen(
		"Find",
		upper_bottom_prompt=(
			f"Found at log {log}, entry {hex(entry)}, page {page}"
		),
		bottom_prompt=(
			"Press enter to go to that location. Press any other key to cancel"
		)
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