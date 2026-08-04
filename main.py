import curses
import modules.user_keypress as usr
import modules.globals as g
import modules.graphics as gfx
import modules.pages as pg

def main(s):
	# stdscr is in modules.globals
	g.stdscr = s

	# Show cursor
	curses.curs_set(1)
	g.cursor_visible = 1

	# Pause at stdscr.getch() until key gets pressed
	g.stdscr.nodelay(False)

	# Screen width and height
	g.MAX_Y, g.MAX_X = g.stdscr.getmaxyx()

	# Loop runs while is_running is True
	g.is_running = True

	while g.is_running:
		# Clear screen
		gfx.draw_base_screen(
			f"Page {pg.current_page}"
		)

		# Babel text can go from row 2 to row g.MAX_Y - 4
		pg.draw_babel()

		# Move cursor to after the ':'
		g.stdscr.move(g.MAX_Y - 1, 1)

		# Refresh screen
		g.stdscr.refresh()

		# Handle key presses
		key = g.stdscr.getch()
		usr.handle_keypress(key)

if __name__ == "__main__":
	curses.wrapper(main)