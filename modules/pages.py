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
	char_buffer = []

	# Starting state for seed
	st = c.PAGES_PER_ENTRY * (c.ENTRIES_PER_LOG * current_log + current_entry)
	st += current_page

	# Max y x
	max_y, max_x = g.babel_win.getmaxyx()
	# Decrement max y for last row
	max_y -= 1

	g.babel_win.clear()

	# Iterate through each pixel
	for y in range(max_y):

		# If buffer is empty, generate a new one
		if len(char_buffer) < max_x:

			# First, generate a very large random number
			st = rand.random(st)

			# Then, split that number into chunks of c.ALPHABET_BITS bits
			# and concat to buffer.
			char_buffer += h.split_into_bits(
				st,
				c.ALPHABET_BITS,
				c.RAND_OUT_BIT_LENGTH
			)

		# Turn indexes into row of chars
		row = char_buffer[0:max_x]
		del char_buffer[0:max_x]
		row = [c.ALPHABET[idx] for idx in row]
		row = "".join(row)

		# Write row
		g.babel_win.addstr(y, 0, row)