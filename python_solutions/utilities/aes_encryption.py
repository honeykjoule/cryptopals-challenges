def aes_decrypt_block(block: bytes, key: bytes) -> bytes:
    key_schedule = key_expansion(key)
    add_round_key(state, key_schedule)
    for round in range(9, 0, -1):
        
    return decrypted_block

def decrypt_aes_ecb(ciphertext: bytes, key: bytes) -> bytes:
    decrypted_text = b''

    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        decrypted_block = aes_decrypt_block(block, key)
        decrypted_text += decrypted_block

    return decrypted_text
