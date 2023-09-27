from constants import S_BOX, INVERSE_S_BOX, RCON

def sub_word(word: bytes) -> bytearray:
    return bytearray([S_BOX[b] for b in word])

def rot_word(word: bytes) -> bytes:
    return word[1:] + word[:1]

def key_expansion(key: bytes) -> bytearray:
    expanded_key = bytearray(4*(10+1)*4)
    expanded_key[:16] = key
    temp = bytearray(4)
    for i in range(4, 44):
        temp = expanded_key[(i-1)*4:i*4]

        if i % 4 == 0:
            temp = sub_word(rot_word(temp))
            temp[0] = temp[0] ^ RCON[i//4]

        for j in range(4):
            expanded_key[i*4+j] = expanded_key[(i-4)*4+j] ^ temp[j]
    return expanded_key


def add_round_key(state: list, round_key: bytes, round_number: int):
    start_idx = round_number * 16
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[start_idx + i * 4 + j]

def inv_shit_rows(state: list):
    for i in range(1, 4):
        state[i] = state[i][-i:] + state[i][:-i]

def inv_sub_bytes(state: list):
    for i in range(4):
        for j in range(4):
            state[i][j] = INVERSE_S_BOX[state[i][j]]

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
