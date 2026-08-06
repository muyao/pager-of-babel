import curses
import config as c

# Check if a string can be turned into an int
def is_int(string: str) -> bool:
	try:
		int(string)
	except:
		return False
	return True

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