import hashlib
import config as c

# Non-reversible round function F
# Takes a half-block integer r and a round key, then hashes it to produce a
# pseudorandom integer of length HALF_BITS
def F(r: int, key: int) -> int:
	# Convert inputs to bytes
	r_bytes = r.to_bytes((c.RAND_HALF_BITS + 7) // 8, byteorder="big")
	k_bytes = key.to_bytes(4, byteorder="big")

	# Hash using SHA-256 (extending via counter if more bits are needed)
	output_bytes = bytearray()
	counter = 0
	needed_bytes = (c.RAND_HALF_BITS + 7) // 8

	while len(output_bytes) < needed_bytes:
		h = hashlib.sha256(
			r_bytes
			+ k_bytes
			+ counter.to_bytes(4, byteorder="big")
		)
		output_bytes.extend(h.digest())
		counter += 1

	# Convert back to an integer masked to exact half bit-length
	res = int.from_bytes(output_bytes[:needed_bytes], byteorder="big")
	return res & c.RAND_HALF_MASK


# Forward Feistel transformation
def random(s: int) -> int:
	# Split input integer into Left and Right halves
	L = s >> c.RAND_HALF_BITS
	R = s & c.RAND_HALF_MASK

	for round_idx in range(c.RAND_ROUNDS):
		key = c.RAND_ROUND_KEYS[round_idx]
		next_L = R
		next_R = L ^ F(R, key)
		L, R = next_L, next_R

	# Combine halves back into a single integer
	return (L << c.RAND_HALF_BITS) | R

# Reverse Feistel transformation
def unrandom(s: int) -> int:
	# Split encrypted state into Left and Right halves
	L = s >> c.RAND_HALF_BITS
	R = s & c.RAND_HALF_MASK

	for round_idx in reversed(range(c.RAND_ROUNDS)):
		key = c.RAND_ROUND_KEYS[round_idx]
		prev_R = L
		prev_L = R ^ F(prev_R, key)
		L, R = prev_L, prev_R

	# Combine halves back into original integer
	return (L << c.RAND_HALF_BITS) | R