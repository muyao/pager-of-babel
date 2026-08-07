import xxhash
import config as c
from bitarray import bitarray

# Non-reversible round function F
# Takes a half-block integer r and a round key, then hashes it to produce a
# pseudorandom integer of length HALF_BITS
def F(r: bitarray, key: int) -> bitarray:
	# Convert inputs to bytes
	r_bytes = r.tobytes()

	# Hash using SHA-256 (extending via counter if more bits are needed)
	output_bytes = bytearray()
	counter = 0

	while len(output_bytes) < c.RAND_HALF_BYTES:
		h1 = xxhash.xxh128(
			r_bytes
			+ counter.to_bytes(4, byteorder="big"),
			seed=key
		)
		counter += 1
		h2 = xxhash.xxh128(
			r_bytes
			+ counter.to_bytes(4, byteorder="big"),
			seed=key
		)
		counter += 1
		output_bytes.extend(h1.digest() + h2.digest())

	# Convert back to an integer masked to exact half bit-length
	res = bitarray(output_bytes)[:len(r)]
	if len(res) < c.RAND_HALF_BITS:
		res[:0] = bitarray(c.RAND_HALF_BITS - len(res))
	return res


# Forward Feistel transformation
def random(s: bitarray) -> bitarray:
	# Split input integer into Left and Right halves
	L = s[:c.RAND_HALF_BITS]
	R = s[c.RAND_HALF_BITS:]
	if len(L) < c.RAND_HALF_BITS:
		L[:0] = bitarray(c.RAND_HALF_BITS - len(L))
	if len(R) < c.RAND_HALF_BITS:
		R[:0] = bitarray(c.RAND_HALF_BITS - len(R))

	for round_idx in range(c.RAND_ROUNDS):
		key = c.RAND_ROUND_KEYS[round_idx]
		next_L = R
		next_R = (L ^ F(R, key))
		L, R = next_L, next_R

	# Combine halves back into a single integer
	return L + R

# Reverse Feistel transformation
def unrandom(s: bitarray) -> bitarray:
	# Split encrypted state into Left and Right halves
	L = s[:c.RAND_HALF_BITS]
	R = s[c.RAND_HALF_BITS:]
	if len(L) < c.RAND_HALF_BITS:
		L[:0] = bitarray(c.RAND_HALF_BITS - len(L))
	if len(R) < c.RAND_HALF_BITS:
		R[:0] = bitarray(c.RAND_HALF_BITS - len(R))

	for round_idx in reversed(range(c.RAND_ROUNDS)):
		key = c.RAND_ROUND_KEYS[round_idx]
		prev_R = L
		prev_L = (R ^ F(prev_R, key))
		L, R = prev_L, prev_R

	# Combine halves back into original integer
	return L + R