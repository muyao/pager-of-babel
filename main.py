import base62
import curses
import config as c
import modules.user_keypress as usr
import modules.globals as g
import modules.graphics as gfx
import modules.pages as pg

def main(s: curses.window) -> int:
	g.init(s)

	# Show cursor
	curses.curs_set(1)

	# Pause at stdscr.getch() until key gets pressed
	g.stdscr.nodelay(False)

	# Loop runs while is_running is True
	g.is_running = True

	while g.is_running:

		# In case log name is too long
		log = base62.encode(pg.current_log)
		if len(log) > c.MAX_LOG_DISPLAY_LENGTH:
			log = f"{log[:7]}..."

		# Clear screen
		gfx.draw_base_screen(
			f"Log {log} - Entry {hex(pg.current_entry)} - Page {pg.current_page}"
		)

		# Babel text can go from row 2 to row g.MAX_Y - 4
		pg.draw_babel()

		# Move cursor to after the ':'
		g.stdscr.move(g.MAX_Y - 1, 1)

		# Show cursor
		curses.curs_set(1)

		# Refresh screen
		g.stdscr.refresh()

		# Handle key presses
		key = g.stdscr.getch()
		usr.handle_keypress(key)

	# Code executed successfully
	return 0

if __name__ == "__main__":
	curses.wrapper(main)