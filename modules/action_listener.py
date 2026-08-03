import modules.command as cmd
import modules.globals as g
import modules.pages as pg

def listen_for_actions():
	key = g.stdscr.getch()
	# Let user enter command if key is :
	if key == ord(':'):

		# Get command input
		command = cmd.input_command()
	
		# Process entered command
		if cmd.process_command(command):

			# Return True to break
			return True

	# Next page if space
	elif key == ord(' '):
		pg.current_page += 1

	# Previous page if b
	elif key == ord('b'):
		pg.current_page -= 1
		if pg.current_page < 0:
			pg.current_page = 0

	# Otherwise return False
	return False