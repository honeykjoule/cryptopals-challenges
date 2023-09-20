from utilities.frequency_analysis import score_text

def fixed_xor(buffer1: bytes, buffer2: bytes) -> bytes:
    if len(buffer1) != len(buffer2):
        raise ValueError('Both buffers should be of equal length')
    xor_result = bytearray()
    for b1, b2 in zip(buffer1, buffer2):
        xor_result.append(b1 ^ b2)
    return bytes(xor_result)

def single_byte_xor(input_bytes: bytes, key:int) -> bytes:
    return bytes([b ^ key for b in input_bytes])

def repeating_key_xor(text_bytes: bytes, key_bytes: bytes) -> bytes:
    encrypted_bytes = bytearray()
    for i, byte in enumerate(text_bytes):
        key_index = i % len(key_bytes)
        encrypted_byte = byte ^ key_bytes[key_index]
        encrypted_bytes.append(encrypted_byte)
    return encrypted_bytes

def detect_single_char_xor(
        byte_array: bytearray,
        frequency_table: dict
    ) -> tuple[int, str]:
    
    best_score = 0
    best_key = -1
    best_decryption = ''

    for key in range(256):
        plaintext_result = ''.join(
            chr(key ^ byte) for byte in byte_array
        )
        current_score = score_text(plaintext_result, frequency_table)
        
        if current_score > best_score:
            best_score = current_score
            best_key = key
            best_decryption = plaintext_result
    
    return best_key, best_decryption
