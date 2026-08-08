import base62
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

	max_y, max_x = g.stdscr.getmaxyx()

	# Write a '>'
	g.stdscr.addstr(max_y - 1, 0, '>')

	# Read up to 32 characters of input
	raw_input = g.stdscr.getstr(max_y - 1, 1, c.MAX_CMD_LENGTH)

	# Hide typed characters
	curses.noecho()

	# Sanitise input before returning
	return raw_input.decode("utf-8").strip()

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
		pg.line_offset = 0
		if pg.current_page < 1:
			pg.current_page = 1
		elif pg.current_page > c.PAGES_PER_ENTRY:
			pg.current_page = c.PAGES_PER_ENTRY

	elif command == 'f' or command == "search":
		search.show_search_screen()

	# Change entry
	elif command.startswith("entry "):
		cmd_body = command[6:]
		if len(cmd_body) > c.MAX_ENTRY_LENGTH:
			raise Exception("Bad entry format")
		cmd_body = cmd_body.replace("-", "")
		try:
			targ_entry = int(cmd_body, base=16)
		except:
			raise Exception("Bad entry format")
		pg.current_entry = targ_entry
		pg.current_page = 1
		pg.line_offset = 0

	elif command.startswith("log "):
		cmd_body = command[4:]
		try:
			targ_log = base62.decode(cmd_body)
		except:
			raise Exception("Bad log format")
		pg.current_log = targ_log
		pg.current_entry = 0
		pg.current_page = 1
		pg.line_offset = 0