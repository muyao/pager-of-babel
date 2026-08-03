import modules.globals as g
import modules.command as cmd

def listen_for_actions():
	# Let user enter command if key is :
	if g.stdscr.getch() == ord(':'):

		# Get command input
		command = cmd.input_command()
	
		# Process entered command
		if cmd.process_command(command):

			# Return True to break
			return True

	# Otherwise return False
	return False