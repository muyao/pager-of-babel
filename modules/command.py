import curses
import config as c
import modules.search as search
import modules.globals as g
import modules.help_manual as help_manual
import modules.helpers as h
import modules.pages as pg

def input_command():
	# Show characters as user types them
	curses.echo()

	# Write a '>'
	g.stdscr.addstr(g.MAX_Y - 1, 0, '>')

	# Read up to 32 characters of input
	raw_input = g.stdscr.getstr(g.MAX_Y - 1, 1, c.MAX_CMD_LENGTH)

	# Hide typed characters
	curses.noecho()

	# Sanitise input before returning
	return raw_input.decode("utf-8").strip().lower()

def process_command(command: str) -> None:
	# Quit if q or quit
	if command == 'q' or command == "quit":
		# Stop running
		g.is_running = False
	
	# Show help screen if help
	elif command == 'h' or command == "help":
		# Show help manual
		help_manual.show_manual()

	elif h.is_int(command):
		pg.current_page = int(command)
		if pg.current_page < 1:
			pg.current_page = 1
		elif pg.current_page > c.PAGES_PER_ENTRY:
			pg.current_page = c.PAGES_PER_ENTRY

	elif command == 'f' or command == "search":
		search.show_search_screen()