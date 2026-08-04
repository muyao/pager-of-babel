import curses
import modules.globals as g
import modules.graphics as gfx
import modules.help as help
import modules.helpers as h
import modules.pages as pg

def input_command():
	# Show characters as user types them
	curses.echo()
	# Show cursor
	curses.curs_set(1)

	# Write a ':'
	g.stdscr.addstr(g.MAX_Y - 1, 0, ':')

	# Read up to 32 characters of input
	raw_input = g.stdscr.getstr(g.MAX_Y - 1, 1, 32)

	# Hide typed characters
	curses.noecho()
	# Hide cursor
	curses.curs_set(0)

	# Sanitise input before returning
	return raw_input.decode("utf-8").strip().lower()

def process_command(command):
	# Quit if q or quit
	# Return True to break
	if command == 'q' or command == "quit":
		return {"should_break": True}
	
	# Show help screen if help
	elif command == 'h' or command == "help":
		# Clear screen
		gfx.draw_base_screen(
			"Help Manual",
			"Press any key to exit help manual"
		)

		# Show help manual
		help.show_manual()

		# Wait until another key is pressed
		g.stdscr.getch()

	elif h.is_int(command):
		if int(command) >= 0:
			pg.current_page = int(command)

	# Return false to not break
	return {"should_break": False}