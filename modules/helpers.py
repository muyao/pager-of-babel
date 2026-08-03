# XOR shift. Default mask is 32 bits
def xor_shift(st, k, m=0xffffffff):
	# Left shift if k > 0
	if k > 0:
		return (st ^ (st << k)) & m

	# Right shift with positive k if k < 0
	else:
		return (st ^ (st >> -k)) & m

# Generate random number with XOR shift
def random(seed):
	# Make sure st is not 0
	# Negative seeds will generate the same output as positive seeds, keep that
	# in mind
	st = abs(seed) + 1

	# 5760 bits
	mask = 0x10 ** 5760 - 1

	# XOR shifting
	st = xor_shift(st, 7, m=mask)
	st = xor_shift(st, -11, m=mask)
	st = xor_shift(st, 173, m=mask)

	# Return final output
	return st

# Check if a string can be turned into an int
def is_int(string):
	try:
		int(string)
		return True
	except:
		return False

# Split a large integer into 4 bit chunks
def split_into_bits(val, chs, m):
	chunks = []
	while val > 0:

		# Bitwise AND val & m returns chs least sig digits
		# We use insert to keep most sig digits at the start
		chunks.insert(0, val & m)

		# Rightshift to remove those digits
		val >>= chs

	# Return
	return chunks