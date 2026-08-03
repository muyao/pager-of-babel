import curses
import modules.action_listener as acl
import modules.globals as g
import modules.graphics as gfx

def main(s):
	# stdscr is from modules.globals
	g.stdscr = s
	# Hide cursor
	curses.curs_set(0)

	# Pause at stdscr.getch() until key gets pressed
	g.stdscr.nodelay(False)

	# Screen width and height
	g.MAX_Y, g.MAX_X = g.stdscr.getmaxyx()

	while True:
		# Clear screen
		gfx.clear_screen(
			"Page X",
			"Press ':' to enter command"
		)

		# Listen for key presses. Break if return is True (when should break,
		# like :q)
		if acl.listen_for_actions():
			break

if __name__ == "__main__":
	curses.wrapper(main)