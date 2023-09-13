from find_keysize import find_keysize
from convert_base64_to_bytes import convert_base64_to_bytes

def repeating_key_XOR(text_byte_array, key_byte_array):
    encrypted_bytes = bytearray()

    for i, byte, in enumerate(text_byte_array):
        key_index = i % len(key_byte_array)
        encrypted_byte = byte ^ key_byte_array[key_index]
        encrypted_bytes.append(encrypted_byte)
    return encrypted_bytes

def detect_single_char_XOR(byte_array):
    frequency_table = {}
    for index, char in enumerate('ETAOIN SHRDLU'):
        frequency_table[char] = 12 - index

    best_score = 0
    best_key = None
    best_decryption = ''

    for key in range(256):
        plaintext_result = ''
        for byte in byte_array:
            xor_byte_result = key ^ byte
            plaintext_result += chr(xor_byte_result)

        current_score = score_text(plaintext_result, frequency_table)
        if current_score > best_score:
            best_score = current_score
            best_key = key
            best_decryption = plaintext_result

    return best_key, best_decryption

def score_text(text, frequency_table):
    score = 0
    for char in text.upper():
        score += frequency_table.get(char, 0)
    return score

def find_repeating_key_xor(ciphertext, keysize):
    blocks = break_into_blocks(ciphertext, keysize)
    transposed_blocks = transpose_blocks(blocks)

    key = []
    for block in transposed_blocks:
        key_byte, _ = detect_single_char_XOR(block)
        key.append(key_byte)

    return bytes(key)

def decrypt_repeating_key_xor(ciphertext, key):
    return repeating_key_XOR(ciphertext, key)


def break_into_blocks(ciphertext, keysize):
    return [ciphertext[i:i+keysize] for i in range(0,len(ciphertext), keysize)]

def transpose_blocks(blocks):
    transposed = []
    for i in range(len(blocks[0])):
        transposed_block = [block[i] for block in blocks if i < len(block)]
        transposed.append(bytes(transposed_block))

    return transposed

def main():

    with open('challenge_data_6.txt', 'r') as file:
        ciphertext_base64 = file.read().strip().replace('\n', '')
        ciphertext = convert_base64_to_bytes(ciphertext_base64)

    keysize = find_keysize()

    key = find_repeating_key_xor(ciphertext, keysize)
    decrypted_text = decrypt_repeating_key_xor(ciphertext, key)

    print(f"Found key: {key.decode('utf-8')}")
    print(f"Decrypted text: {decrypted_text}")

if __name__ == '__main__':
    main()
