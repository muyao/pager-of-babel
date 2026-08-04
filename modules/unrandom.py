import config as c

# Reverse left shift
def reverse_left(s, k):
	# Mask. If k=4, mask=0b1111
	m = 2 ** k - 1

	# Keep track of how many bits we shifted to know when to stop
	bits_shifted = 0

	while bits_shifted < c.XOR_BIT_LENGTH:

		# Get bits of s for xor
		xor = (s & m) << k

		# XOR s with xor << k
		s = (s ^ xor) & c.XOR_MASK

		# Increase bits shifted
		bits_shifted += k

		# Shift mask over by k bits
		m <<= k

	# Return reversed state
	return s

# Reverse right shift
def reverse_right(s, k):
	# Mask. If k=4, mask=0b1111
	m = 2 ** k - 1
	# Align mask so that msd of mask at the same place as msd of s
	m <<= c.XOR_BIT_LENGTH - k

	# Keep track of how many bits we shifted to know when to stop
	bits_shifted = 0

	while bits_shifted < c.XOR_BIT_LENGTH:

		# Get bits of s for xor
		xor = (s & m) >> k

		# XOR s with xor << k
		s = (s ^ xor) & c.XOR_MASK

		# Increase bits shifted
		bits_shifted += k

		# Shift mask over by k bits
		m >>= k

	# Return reversed state
	return s

# Reverse xor shift
def get_seed(s):
	# Reverse so that last shift comes first
	# Avoid using .reverse() because it also reverses XOR_SHIFTS
	shifts = c.XOR_SHIFTS[::-1]

	# Then, for each shift
	for k in shifts:

		# Left shift
		if k > 0:
			s = reverse_left(s, k)

		# Right shift
		else:
			s = reverse_right(s, -k)

	# Return previous state
	return s