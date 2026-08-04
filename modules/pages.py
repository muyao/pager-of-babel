import config as c
import modules.globals as g
import modules.helpers as h
import modules.random as rand

# Track current page
current_page = 960

# Track current log
current_log = 45194800266577031337190087523556954983344263359572393147069306276016698632644772738014089765989625598415917663650903725311054598241435687532279658540993378388790340656691186180869599830092807484026523103737138689194454045932604162246942317603121663479015720383661133921429894079601236593839575289190894059

def draw_babel():
	# Reset buffer
	text_buffer = []

	# Starting state for seed
	st = c.PAGES_PER_LOG * current_log + current_page

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