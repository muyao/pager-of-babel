import curses

# Global variables
stdscr = None
MAX_X = None
MAX_Y = None
is_running = None

# Here actually give them a value
def init(s: curses.window) -> None:
	# Screen
	global stdscr
	stdscr = s

	# Width and height
	global MAX_Y
	global MAX_X
	MAX_Y, MAX_X = stdscr.getmaxyx()

	# Is running
	global is_running
	is_running = False