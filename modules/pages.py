import json
import config as c
import modules.globals as g
import modules.helpers as h
import modules.random as rand
from pathlib import Path

current_page = 0
current_entry = 0
current_log = 0
line_offset = 0

# Read initial seed from resources/seed.json
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

	# Seed for first page
	st = (
		c.PAGES_PER_ENTRY * (c.ENTRIES_PER_LOG * current_log + current_entry)
		+ current_page
	)

	# Max y x
	max_y, max_x = g.babel_win.getmaxyx()
	# Decrement max y for last row
	max_y -= 1

	g.babel_win.clear()

	# First page
	draw_page(st, max_y, max_x, line_offset)

	# Stop if only one page is visible
	if line_offset == 0:
		return

	# Seed for second page
	st = (
		c.PAGES_PER_ENTRY * (c.ENTRIES_PER_LOG * current_log + current_entry)
		+ current_page + 1
	)

	# Second page
	draw_page(st, max_y, max_x, line_offset - max_y)

def draw_page(st: int, max_y: int, max_x: int, off: int) -> None:

	char_buffer = []

	# Iterate through each pixel
	for y in range(max_y):

		# If buffer is exhausted, concat more
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

		# Stop if row is offscreen (bottom)
		if y - off >= max_y:
			return

		# Turn indexes into row of chars
		# Skip if row is offscreen (top)
		if y - off >= 0:
			row = char_buffer[0:max_x]
			row = [c.ALPHABET[idx] for idx in row]
			row = "".join(row)
			# Write row
			g.babel_win.addstr(y - off, 0, row)

		del char_buffer[0:max_x]