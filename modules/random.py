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
	for k in c.XOR_SHIFTS:
		st = single_xor_shift(st, k, mask)

	# Return final output
	return st