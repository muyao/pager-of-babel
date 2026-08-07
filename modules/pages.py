import json
import config as c
import modules.globals as g
import modules.random as rand
from pathlib import Path

current_page = 0
current_entry = 0
current_log = 0
line_offset = 0

# Cache the pages to make scrolling faster
cached_ids = [0, 0]
cached_data = [0, 0]
cached_last_st = [0, 0]

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
	draw_page(st, max_y, max_x, line_offset, 0)

	# Stop if only one page is visible
	if line_offset == 0:
		return

	# Seed for second page
	st = (
		c.PAGES_PER_ENTRY * (c.ENTRIES_PER_LOG * current_log + current_entry)
		+ current_page + 1
	)

	# Second page
	draw_page(st, max_y, max_x, line_offset - max_y, 1)

def draw_page(
	st: int, max_y: int, max_x: int, off: int, cache_idx: int
) -> None:

	if st == cached_ids[cache_idx]:
		char_buffer = cached_data[cache_idx]
		st = cached_last_st[cache_idx]
	else:
		char_buffer = 1
		cached_data[cache_idx] = 1
		cached_ids[cache_idx] = st
		cached_last_st[cache_idx] = 0

	# Iterate through each pixel
	for y in range(max_y):

		# Stop if row is offscreen (bottom)
		if y - off >= max_y:
			return

		for x in range(max_x):

			# If buffer is exhausted, generate new one
			if char_buffer.bit_length() - 1 < c.ALPHABET_BITS:

				# Generate next chunk
				st = rand.random(st)

				# Add st to char_buffer
				old_len = char_buffer.bit_length() - 1
				old_mask = (1 << old_len) - 1
				# Remove the 1 at the beginning (0b101110 -> 0b01110)
				char_buffer &= old_mask
				# Append st to char_buffer
				char_buffer |= st << old_len
				# Re-add the 1 to the beginning (0b01110 -> 0b101110)
				char_buffer |= old_mask + 1

				# Do the same for cached_data
				old_len = cached_data[cache_idx].bit_length() - 1
				old_mask = (1 << old_len) - 1
				# Remove the 1 at the beginning (0b101110 -> 0b01110)
				cached_data[cache_idx] &= old_mask
				# Append st to char_buffer
				cached_data[cache_idx] |= st << old_len
				# Re-add the 1 to the beginning (0b01110 -> 0b101110)
				cached_data[cache_idx] |= old_mask + 1

				# Remember last st to be able to generate more chunks
				cached_last_st[cache_idx] = st
			
			# Only if row is not offscreen (top)
			if y - off >= 0:
				# Write char
				char = c.ALPHABET[char_buffer & c.ALPHABET_CHAR_MASK]
				g.babel_win.addstr(y - off, x, char)

			char_buffer >>= c.ALPHABET_BITS