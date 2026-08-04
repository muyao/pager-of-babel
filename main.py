import curses
import modules.action_listener as acl
import modules.globals as g
import modules.graphics as gfx
import modules.pages as pg

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
		gfx.draw_base_screen(
			f"Page {pg.current_page}",
			"Press ':' to enter command"
		)

		# Babel text can go from row 2 to row g.MAX_Y - 4
		pg.draw_babel()

		# Refresh screen
		g.stdscr.refresh()

		# Listen for key presses. Break if return is True (when should break,
		# like :q)
		actions_return = acl.listen_for_actions()
		if actions_return["should_break"]:
			break

if __name__ == "__main__":
	curses.wrapper(main)