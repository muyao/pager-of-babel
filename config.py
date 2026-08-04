# Alphabet to use. Must be 32 chars long
ALPHABET = "abcdefghijklmnopqrstuvwxyz    ,."

# How many bits output by xor shift
XOR_BIT_LENGTH = 2048

# XOR mask to only take lowest bits
XOR_MASK = 2 ** XOR_BIT_LENGTH - 1

# How many times it should roll seed
START_ROLL = 16