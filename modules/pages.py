import modules.config as c
import modules.globals as g
import modules.helpers as h

# Track current page
current_page = 0

def draw_babel():
	# Reset buffer
	text_buffer = []

	# Starting state for seed
	st = current_page

	# Randomise st a bit first
	for i in range(128):
		st = h.random(st)

	# Whether it should write the next letter in highcaps
	should_capitalise = True

	# Iterate through each pixel
	for y in range(g.MAX_Y - 5):
		for x in range(g.MAX_X):

			# If buffer is empty, generate a new one
			if len(text_buffer) <= 0:
				# First, generate a very large random number
				st = h.random(st)
				# Then, split that number into chunks of 6 bits and write into
				# buffer
				text_buffer = h.split_into_bits(st, 6, 0b111111)

			# Use whichever number is at the start of text_buffer. Capitalise
			# if needed.
			if should_capitalise:
				letter = c.ALPHABET[text_buffer[0]].upper()
			else:
				letter = c.ALPHABET[text_buffer[0]]

			# Delete it from buffer so we don't use it again
			del text_buffer[0]

			# Write letter
			g.stdscr.addstr(y + 2, x, letter)

			# Caps logic
			should_capitalise = False
			#if letter == ".":
			#	should_capitalise = True
			#elif letter != " ":
			#	should_capitalise = False






# x*(y-5)