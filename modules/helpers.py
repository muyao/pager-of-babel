import config as c

# XOR shift
def single_xor_shift(st, k, m):
	# Shift left if k > 0, else shift right
	shifted = st << k if k > 0 else st >> -k

	# Return
	return (st ^ shifted) & m

# Generate random number with XOR shift
def random(st):
	# If state is 0 or negative, throw error
	if st <= 0:
		raise Exception("Seed cannot be zero or negative")

	# How many bits long output should be
	mask = c.XOR_MASK

	# XOR shifting
	st = single_xor_shift(st, 7, mask)
	st = single_xor_shift(st, -11, mask)
	st = single_xor_shift(st, 173, mask)

	# Return final output
	return st

# Check if a string can be turned into an int
def is_int(string):
	try:
		int(string)
	except:
		return False
	return True

# Split a large integer into chs bit long chunks
def split_into_bits(val, chs, tot_bits):
	chunks = []

	# We track bits left separately in case number starts with 0s
	bits_left = tot_bits

	# Repeat while we still have bits left
	while bits_left > 0:

		# Bitwise AND val & m returns chs least sig digits
		# We use insert to keep most sig digits at the start
		chunks.insert(0, val & (2 ** chs - 1))

		# Rightshift to remove those digits
		val >>= chs

		# Decrease bits_left by chunk size
		bits_left -= chs

	# Return without first element because it tends to be less than chs long
	return chunks[1:]