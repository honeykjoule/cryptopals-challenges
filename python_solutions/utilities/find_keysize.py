from utilities.frequency_analysis import generate_frequency_table
from utilities.xor_operations import detect_single_char_xor

def calculate_hamming_distance(byte_one: bytes, byte_two: bytes) -> int:
    if len(byte_one) != len(byte_two):
        raise ValueError(
            'Both byte sequences must be equal length for hamming distance'
        )
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
                min_length = min(len(keysized_blocks[i]), len(keysized_blocks[j]))
                block1 = keysized_blocks[i][:min_length]
                block2 = keysized_blocks[j][:min_length]
                cumulative_hamming_distance += calculate_hamming_distance(
                    block1,
                    block2
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
    frequency_table = generate_frequency_table()
    for i in range(len(blocks[0])):
        transposed_block = [block[i] for block in blocks if i < len(block)]
        transposed_blocks.append(transposed_block)
    key_sequence = []
    for block in transposed_blocks:
        key_byte, _ = detect_single_char_xor(block, frequency_table)
        key_sequence.append(key_byte)
    return bytes(key_sequence)
