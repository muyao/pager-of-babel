import math

# Alphabet to use. Must be 32 chars long
ALPHABET = "    abcdefghijklmnopqrstuvwxyz,."

# How many bits long the alphabet is.
ALPHABET_BITS = int(math.log2(len(ALPHABET)))

# How many bits outputted by random
RAND_OUT_BIT_LENGTH = 32768

# Half len
RAND_HALF_BITS = RAND_OUT_BIT_LENGTH // 2

# Half mask
RAND_HALF_MASK = (1 << RAND_HALF_BITS) - 1

# Rand rounds for prng
RAND_ROUNDS = 4

# Keys for PRNG
RAND_ROUND_KEYS = [0x1a2b3c4d, 0x5e6f7abb, 0x9c0d1e2f, 0x3a4b5c6d]

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
MAX_SEARCH_LENGTH = RAND_OUT_BIT_LENGTH // ALPHABET_BITS

# Max length of commands
MAX_CMD_LENGTH = 32