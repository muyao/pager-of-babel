import curses
import modules.globals as g
import modules.help as help
import modules.helpers as h
import modules.pages as pg

def input_command():
	# Show characters as user types them
	curses.echo()

	# Write a '>'
	g.stdscr.addstr(g.MAX_Y - 1, 0, '>')

	# Read up to 32 characters of input
	raw_input = g.stdscr.getstr(g.MAX_Y - 1, 1, 32)

	# Hide typed characters
	curses.noecho()

	# Sanitise input before returning
	return raw_input.decode("utf-8").strip().lower()

def process_command(command):
	# Quit if q or quit
	if command == 'q' or command == "quit":
		# Stop running
		g.is_running = False
	
	# Show help screen if help
	elif command == 'h' or command == "help":
		# Show help manual
		help.show_manual()

	elif h.is_int(command):
		if int(command) > 0:
			pg.current_page = int(command)