import modules.globals as g

def clear_screen(bottom_prompt):
	# Clear screen
	g.stdscr.clear()
	
	# Title
	g.stdscr.addstr(0, int(g.MAX_X / 2) - 9, "The Pager of Babel")

	# Bottom prompt
	g.stdscr.addstr(g.MAX_Y - 2, 0, bottom_prompt)

	# Refresh screen
	g.stdscr.refresh()