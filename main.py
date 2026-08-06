import base62
import curses
import config as c
import modules.user_keypress as usr
import modules.globals as g
import modules.graphics as gfx
import modules.helpers as h
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

		# Crash if window gets resized
		if g.stdscr.getmaxyx() != (g.MAX_Y, g.MAX_X):
			raise Exception("Window resized")

		# Graphics stuff
		gfx.draw_title()
		log_str = base62.encode(pg.current_log)
		log_str = h.cut_off_end(log_str, c.MAX_LOG_DISPLAY_LENGTH)
		entry_str = hex(pg.current_entry)
		info = c.INFO_MSG(log_str, entry_str, pg.current_page)
		gfx.draw_info(info)
		gfx.draw_footer()

		# Babel text can go from row 2 to row g.MAX_Y - 4
		pg.draw_babel()

		# Move cursor to after the ':'
		g.stdscr.move(g.MAX_Y - 1, 1)

		# Show cursor
		curses.curs_set(1)

		# Refresh screen
		g.info_win.refresh()
		g.babel_win.refresh()
		g.footer_win.refresh()

		# Handle key presses
		key = g.stdscr.getch()
		usr.handle_keypress(key)

	# Code executed successfully
	return 0

if __name__ == "__main__":
	curses.wrapper(main)