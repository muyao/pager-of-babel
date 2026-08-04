import config as c
import modules.command as cmd
import modules.find as find
import modules.globals as g
import modules.help_manual as help_manual
import modules.pages as pg

def handle_keypress(key):
	# Let user enter command if key is :
	if key == ord(':'):

		# Get command input
		command = cmd.input_command()
	
		# Process entered command
		cmd.process_command(command)

	# Next page if space
	elif key == ord(' '):
		pg.current_page += 1

		# Page# cannot go past PAGES_PER_LOG
		if pg.current_page > c.PAGES_PER_ENTRY:
			pg.current_page = c.PAGES_PER_ENTRY

	# Previous page if b
	elif key == ord('b'):
		pg.current_page -= 1

		# Make sure page is at least 1
		if pg.current_page < 1:
			pg.current_page = 1

	elif key == ord('q'):
		# Stop running
		g.is_running = False

	elif key == ord('h'):
		# Show help manual
		help_manual.show_manual()

	elif key == ord('f'):
		# Find screen
		find.show_find_screen()