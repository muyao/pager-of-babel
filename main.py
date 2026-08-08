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

	max_y, max_x = g.stdscr.getmaxyx()

	if max_x < 80:
		raise Exception("Window too small. Must be at least 80 chars wide")


	# Show cursor
	curses.curs_set(1)

	# Pause at stdscr.getch() until key gets pressed
	g.stdscr.nodelay(False)

	# Loop runs while is_running is True
	g.is_running = True

	while g.is_running:

		# Crash if window gets resized
		if g.stdscr.getmaxyx() != (max_y, max_x):
			raise Exception("Window resized")

		# Graphics stuff
		gfx.draw_on_window(g.title_win, 0, 0, c.TITLE)
		# Turn int log into displayed log
		log_str = base62.encode(pg.current_log)
		log_str = h.cut_off_end(log_str, c.MAX_LOG_DISPLAY_LENGTH)
		# Turn int entry into displayed entry
		entry_str = hex(pg.current_entry)
		entry_str = f"{entry_str[2:6]}-{entry_str[6:10]}"
		info = c.INFO_MSG(log_str, entry_str, pg.current_page, pg.line_offset)
		gfx.draw_info(info)
		gfx.draw_on_window(g.footer_win, 0, 0, ':')

		# Babel text can go from row 2 to row max_y - 4
		pg.draw_babel()

		# Move cursor to after the ':'
		g.stdscr.move(max_y - 1, 1)

		# Show cursor
		curses.curs_set(1)

		g.babel_win.noutrefresh()

		# Refresh all
		curses.doupdate()

		# Handle key presses
		key = g.stdscr.getch()
		usr.handle_keypress(key)

	# Code executed successfully
	return 0

if __name__ == "__main__":
	curses.wrapper(main)