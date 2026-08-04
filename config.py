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

# Max log name length
MAX_LOG_LENGTH = 16

# Amount of pages per log
PAGES_PER_LOG = 10 ** MAX_PAGE_LENGTH - 1

# Max length of search phrase
MAX_SEARCH_LENGTH = 200
