import json
import config as c
import modules.globals as g
import modules.helpers as h
import modules.random as rand
from pathlib import Path

# Track current page
current_page = 0

# Track current entry
current_entry = 0

# Track current log
current_log = 0

with open(
	Path(__file__).resolve().parent.parent / "resources" / "seed.json",
	"r"
) as f:
	data = json.load(f)
	current_page = int(data["page"], base=16)
	current_entry = int(data["entry"], base=16)
	current_log = int(data["log"], base=16)
	del data

def draw_babel() -> None:
	# Reset buffer
	text_buffer = []

	# Starting state for seed
	st = c.PAGES_PER_ENTRY * (c.ENTRIES_PER_LOG * current_log + current_entry)
	st += current_page

	# Create subwindow, 1 row more than needed (bottom right corner)
	win = g.stdscr.subwin(g.MAX_Y - 3, g.MAX_X, 2, 0)
	# Max y x
	max_y, max_x = win.getmaxyx()
	# Decrement max y for last row
	max_y -= 1

	# Iterate through each pixel
	for y in range(max_y):
		for x in range(max_x):

			# If buffer is empty, generate a new one
			if len(text_buffer) == 0:
				# First, generate a very large random number
				st = rand.random(st)
				# Then, split that number into chunks of c.ALPHABET_BITS bits
				# and write into buffer.
				text_buffer = h.split_into_bits(
					st,
					c.ALPHABET_BITS,
					c.RAND_OUT_BIT_LENGTH
				)

			# Use whichever number is at the start of text_buffer
			letter = c.ALPHABET[text_buffer[0]]
			# Delete it from buffer so we don't use it again
			del text_buffer[0]

			# Write letter
			win.addstr(y, x, letter)