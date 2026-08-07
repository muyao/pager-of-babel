import curses
import math

# Alphabet to use. Must be 32 chars long
ALPHABET = "    abcdefghijklmnopqrstuvwxyz,."

# How many bits long the alphabet is.
ALPHABET_BITS = int(math.log2(len(ALPHABET)))

# How many bits outputted by random
RAND_OUT_BIT_LENGTH = 1 << 5

# Half len
RAND_HALF_BITS = RAND_OUT_BIT_LENGTH // 2

# Half mask
RAND_HALF_MASK = (1 << RAND_HALF_BITS) - 1

# Half bytes
RAND_HALF_BYTES = (RAND_HALF_BITS + 7) // 8

# Rand rounds for prng
RAND_ROUNDS = 4

# Keys for PRNG
RAND_ROUND_KEYS = [0x1a2b3c4d, 0x5e6f7abb, 0x9c0d1e2f, 0x3a4b5c6d]

# Max page name length
MAX_PAGE_LENGTH = 3

# Max entry name length
MAX_ENTRY_LENGTH = 8

# Max log name length
MAX_LOG_DISPLAY_LENGTH = 20

# Amount of pages per log
PAGES_PER_ENTRY = 10 ** MAX_PAGE_LENGTH - 1

# Amount of entries per log
ENTRIES_PER_LOG = 16 ** MAX_ENTRY_LENGTH - 1

# Max length of search phrase
MAX_SEARCH_LENGTH = RAND_OUT_BIT_LENGTH // ALPHABET_BITS

# Max length of commands
MAX_CMD_LENGTH = 32

# Fancy Paint Styles
FANCY_STYLES = {
	'n': curses.A_NORMAL, 'b': curses.A_BOLD, 'u': curses.A_UNDERLINE
}

# Escape char char for fancy
FANCY_ESCAPE = '?'

# Title that gets displayed in the top left corner
TITLE = "?bThe Pager of Babel?n"

INFO_MSG = lambda log, entry, page, line: (
	f"Log ?u{log}?n    Entry ?u{entry}?n    Page ?u{page}?n    Line ?u{line}?n"
)