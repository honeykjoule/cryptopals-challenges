def key_expansion(key: bytes) -> list:
    #TODO: implement
    return []

def add_round_key(state: list, round_key: bytes, round_number: int):
    pass #TODO implement

def inv_shit_rows(state: list):
    pass #TODO implement

def inv_sub_bytes(state: list):
    pass #TODO implement

def inv_mix_columns(state: list):
    pass #TODO implement

def convert_state_to_bytes(state: list):
    pass #TODO implement

def aes_decrypt_block(block: bytes, key: bytes) -> bytes:
    
    state = []
    key_schedule = key_expansion(key)
    
    add_round_key(state, key_schedule, 10)
    
    for round in range(9, 0, -1):
        inv_shit_rows(state)
        inv_sub_bytes(state)
        add_round_key(state, key_schedule, round)
        inv_mix_columns(state)

    inv_shit_rows(state)
    inv_sub_bytes(state)
    add_round_key(state, key_schedule, 0)

    decrypted_block = convert_state_to_bytes(state)
        
    return decrypted_block

def decrypt_aes_ecb(ciphertext: bytes, key: bytes) -> bytes:
    decrypted_text = b''

    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        decrypted_block = aes_decrypt_block(block, key)
        decrypted_text += decrypted_block

    return decrypted_text
