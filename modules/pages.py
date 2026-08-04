import config as c
import modules.globals as g
import modules.helpers as h
import modules.random as rand

# Track current page
current_page = 524

# Track current entry
current_entry = 1570273697

# Track current log
current_log = 23908342998761355023511331478589481443787430013506081402175051559321781332155686087769515897337062082391183849441184021580880715754542844489816538170099452032343391041531928383071685280066290635281302442203079152429702905439389268761483906007494850379087786775119647218940613600578308356079002680

def draw_babel():
	# Reset buffer
	text_buffer = []

	# Starting state for seed
	st = c.PAGES_PER_ENTRY * (c.ENTRIES_PER_LOG * current_log + current_entry) + current_page

	# Randomise st a bit first so that st will be large
	for i in range(c.START_ROLL):
		st = rand.random(st)

	# Iterate through each pixel
	for y in range(g.MAX_Y - 4):
		for x in range(g.MAX_X):

			# If buffer is empty, generate a new one
			if len(text_buffer) == 0:
				# First, generate a very large random number
				st = rand.random(st)
				# Then, split that number into chunks of 5 bits and write into
				# buffer.
				text_buffer = h.split_into_bits(st, 5, c.XOR_BIT_LENGTH)

			# Use whichever number is at the start of text_buffer
			letter = c.ALPHABET[text_buffer[0]]
			# Delete it from buffer so we don't use it again
			del text_buffer[0]

			# Write letter
			g.stdscr.addstr(y + 2, x, letter)