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

def show_search_screen() -> None:

	gfx.draw_info("Leave empty to cancel    ?bSearch?n")
	gfx.draw_on_window(g.footer_win, 0, 0, "")
	curses.curs_set(1)

	g.babel_win.clear()

	# Wrap the window in a Textbox box manager
	box = Textbox(g.babel_win, insert_mode=True)

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

	# Search
	found_location = search(raw_input)

	display_found(found_location)

def search(raw_input: str) -> tuple[int, int, int]:

	# Clear screen
	gfx.draw_info("Searching...    ?bSearch?n")

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
			(c.RAND_OUT_BIT_LENGTH // c.ALPHABET_BITS) - len(sanitised_input)
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

	log_str = base62.encode(log)
	log_str = h.cut_off_end(log_str, c.MAX_LOG_DISPLAY_LENGTH)

	entry_str = hex(entry)

	g.babel_win.clear()
	gfx.addstrf(g.babel_win, 0, 0, "?bFound at:?n")
	gfx.addstrf(g.babel_win, 1, 0, f"Log ?u{log_str}?n")
	gfx.addstrf(g.babel_win, 2, 0, f"Entry ?u{entry_str}?n")
	gfx.addstrf(g.babel_win, 3, 0, f"Page ?u{page}?n")
	gfx.addstrf(
		g.babel_win,
		5,
		0,
		"Press ?bEnter?n to go to that location. Press any other key to cancel"
	)

	gfx.draw_info("?bSearch?n")
	gfx.draw_on_window(g.footer_win, 0, 0, ':')

	g.stdscr.move(g.stdscr.getmaxyx()[0] - 1, 1)
	curses.curs_set(1)

	g.babel_win.noutrefresh()

	curses.doupdate()

	# Listen for user input
	key = g.stdscr.getch()
	if key != ord('\n'):
		return

	pg.current_log, pg.current_entry, pg.current_page = found_location
	pg.line_offset = 0