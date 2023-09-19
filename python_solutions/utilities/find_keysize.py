def calculate_hamming_distance(byte_one: bytes, byte_two: bytes) -> int:
    if len(byte_one) != len(byte_two):
        return -1
    xor_results = [a ^ b for a, b, in zip(byte_one, byte_two)]
    hamming_distance = sum(bin(x).count('1') for x in xor_results)
    return hamming_distance

def find_keysize(ciphertext: bytes) -> int:
    scored_keysize_values = {}
    for keysize in range(2, 41):
        keysized_blocks = [
            ciphertext[i:i+keysize] 
            for i in range(0, len(ciphertext), keysize)
        ]
        cumulative_hamming_distance = 0
        number_of_blocks = 0
        for i in range(len(keysized_blocks) - 1):
            for j in range(i+1, len(keysized_blocks)):
                cumulative_hamming_distance += calculate_hamming_distance(
                    keysized_blocks[i],
                    keysized_blocks[j]
                )
                number_of_blocks += 1

        scored_keysize_values[keysize] = (
            (cumulative_hamming_distance / number_of_blocks) / keysize
        )
    best_keysize = min(scored_keysize_values, key=scored_keysize_values.get)
    return best_keysize

def find_repeating_key(ciphertext: bytes, keysize: int) -> bytes:
    blocks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]
    transposed_blocks = []
    for i in range(len(blocks[0])):
        transposed_block = [block[i] for block in blocks if i < len(block)]
        transposed_blocks.append(transposed_block)
    key_sequence = []
    for block in transposed_blocks:
        key_byte, _ = detect_single_character_xor(block)
        key_sequence.append(key_byte)
    return bytes(key_sequence)
