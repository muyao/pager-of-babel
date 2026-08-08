import curses
import config as c
import modules.command as cmd
import modules.search as search
import modules.globals as g
import modules.help_manual as help_manual
import modules.pages as pg

def handle_keypress(key: int) -> None:

	max_y, max_x = g.babel_win.getmaxyx()
	max_y -= 1

	if key == ord(':'):
		# Get command input
		command = cmd.input_command()
	
		# Process entered command
		cmd.process_command(command)

	elif key in (ord(' '), ord('f'), ord('z')):
		pg.current_page += 1

		# Page# cannot go past PAGES_PER_LOG
		if pg.current_page > c.PAGES_PER_ENTRY:
			pg.current_page = c.PAGES_PER_ENTRY
		if pg.current_page >= c.PAGES_PER_ENTRY:
			pg.line_offset = 0

	elif key in (ord('b'), ord('w')):
		pg.current_page -= 1

		# Make sure page is at least 1
		if pg.current_page < 1:
			pg.current_page = 1
			pg.line_offset = 0

	elif key == ord('q'):
		# Stop running
		g.is_running = False

	elif key == ord('h'):
		# Show help manual
		help_manual.show_manual()

	elif key == ord('f'):
		# Find screen
		search.show_search_screen()

	elif key in (ord('j'), ord('e'), curses.KEY_DOWN):
		# Stop if we are at the end
		if pg.current_page == c.PAGES_PER_ENTRY:
			return

		pg.line_offset += 1
		if pg.line_offset == max_y:
			pg.line_offset = 0
			pg.current_page += 1

	elif key in (ord('k'), ord('y'), curses.KEY_UP):
		# Stop if we reach page 1
		if pg.current_page == 1 and pg.line_offset == 0:
			return

		pg.line_offset -= 1
		if pg.line_offset < 0:
			pg.line_offset = max_y - 1
			pg.current_page -= 1