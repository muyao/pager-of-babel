import json
import config as c
import modules.globals as g
import modules.random as rand
from pathlib import Path
from bitarray import bitarray
from bitarray.util import ba2int
from bitarray.util import int2ba

from debug import DebugLog
log = DebugLog()

current_page = 0
current_entry = 0
current_log = 0
line_offset = 0

# Cache the pages to make scrolling faster
cached_ids = [0, 0]
cached_data: bitarray = [bitarray(), bitarray()]
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

	log.log("-"* 80)

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

	# If starting state is known, read from cache
	if st == cached_ids[cache_idx]:
		char_buffer = cached_data[cache_idx].copy()
		st = cached_last_st[cache_idx]

	# Otherwise, start from beginning and clear cache slot
	else:
		char_buffer = bitarray()
		cached_data[cache_idx] = bitarray()
		cached_ids[cache_idx] = st
		cached_last_st[cache_idx] = 0

	# Iterate through each pixel
	for y in range(max_y):

		# Stop if row is offscreen (bottom)
		if y - off >= max_y:
			return

		for x in range(max_x):

			# If buffer is exhausted, generate new one
			if len(char_buffer) < c.ALPHABET_BITS:

				# Generate next chunk
				st = rand.random(st)

				# Add st to char_buffer and cache
				st_ba = int2ba(st)
				pad_len = -len(st_ba) % c.ALPHABET_BITS
				st_ba[:0] = bitarray(pad_len)
				char_buffer.extend(st_ba)
				cached_data[cache_idx].extend(st_ba)
				log.log(f"{line_offset}: {st_ba}")

				# Remember last st to be able to generate more chunks
				cached_last_st[cache_idx] = st
			
			# Only if row is not offscreen (top)
			if y - off >= 0:
				# Write char
				char = c.ALPHABET[ba2int(char_buffer[:c.ALPHABET_BITS])]
				g.babel_win.addstr(y - off, x, char)

			# Remove already used bits
			del char_buffer[:c.ALPHABET_BITS]