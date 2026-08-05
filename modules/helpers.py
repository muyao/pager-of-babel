import curses
import config as c

# Check if a string can be turned into an int
def is_int(string: str) -> bool:
	try:
		int(string)
	except:
		return False
	return True

# Split a large integer into chs bit long chunks
def split_into_bits(val: int, chs: int, tot_bits: int) -> list[int]:
	chunks = []

	# We track bits left separately in case number starts with 0s
	bits_left = tot_bits

	# Repeat while we still have bits left
	while bits_left > 0:

		# Bitwise AND val & m returns chs least sig digits
		# We use insert to keep most sig digits at the start
		chunks.insert(0, val & (2 ** chs - 1))

		# Rightshift to remove those digits
		val >>= chs

		# Decrease bits_left by chunk size
		bits_left -= chs

	# Return without first element because it tends to be less than chs long
	return chunks[1:]

# Limit a string to x length
def cut_off_end(string: str, max_len: int, three_dots: str = "\u2026") -> str:
	if len(string) <= max_len:
		return string
	return string[:max_len - len(three_dots)] + three_dots

# Strip a string from fancy escape sequences
def no_escapes(string: str) -> str:
	result = []
	# Convert string into an iterator to manually control loop progression
	chars = iter(string)

	for char in chars:
		if char == c.FANCY_ESCAPE:
			# Skip the escape character and consume the next character to skip
			# it too
			next(chars, None)
		else:
			result.append(char)

	return "".join(result)

# True length of a string without fancy escapes
def true_len(string: str) -> int:
	return len(no_escapes(string))

# Termination check for textbox
def terminate_check(key: int) -> int:
	if key == ord('\n'):
		return 7
	elif key == curses.KEY_DOWN:
		return curses.KEY_RIGHT
	elif key == curses.KEY_UP:
		return curses.KEY_LEFT
	return key