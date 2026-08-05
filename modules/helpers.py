# Check if a string can be turned into an int
def is_int(string: str) -> bool:
	try:
		int(string)
	except:
		return False
	return True

# Split a large integer into chs bit long chunks
def split_into_bits(val: int, chs: int, tot_bits: int) -> list[int]:
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