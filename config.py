# Alphabet to use. Must be 32 chars long
ALPHABET = "    abcdefghijklmnopqrstuvwxyz,."

# How many bits output by xor shift
XOR_BIT_LENGTH = 1024

# XOR mask to only take lowest bits
XOR_MASK = 2 ** XOR_BIT_LENGTH - 1

# How much it should shift. Positive values are left shift
XOR_SHIFTS = [7, -11, 173]

# How many times it should roll seed
START_ROLL = 16

# Max page name length
MAX_PAGE_LENGTH = 3

# Max entry name length
MAX_ENTRY_LENGTH = 8

# Max log name length
MAX_LOG_DISPLAY_LENGTH = 10

# Amount of pages per log
PAGES_PER_ENTRY = 10 ** MAX_PAGE_LENGTH - 1

# Amount of entries per log
ENTRIES_PER_LOG = 16 ** MAX_ENTRY_LENGTH - 1

# Max length of search phrase
MAX_SEARCH_LENGTH = 200

# Max length of commands
MAX_CMD_LENGTH = 32