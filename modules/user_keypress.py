import modules.command as cmd
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

	# Previous page if b
	elif key == ord('b'):
		pg.current_page -= 1

		# Make sure page is at least 1
		if pg.current_page < 1:
			pg.current_page = 1