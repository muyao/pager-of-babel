import curses
import modules.command as cmd
import modules.globals as g
import modules.graphics as gfx

def main(s):
	# stdscr is from modules.globals
	g.stdscr = s
	# Hide cursor
	curses.curs_set(0)

	# Pause at stdscr.getch() until key gets pressed
	g.stdscr.nodelay(False)

	# Screen width and height
	g.MAX_Y, g.MAX_X = g.stdscr.getmaxyx()

	while True:
		# Clear screen
		gfx.clear_screen("Press ':' to enter command")

		# Listen for key presses
		# Let user enter command if key is :
		if g.stdscr.getch() == ord(':'):
			# Get command input
			command = cmd.input_command()

			# Process entered command
			if cmd.process_command(command):
				break

if __name__ == "__main__":
	curses.wrapper(main)