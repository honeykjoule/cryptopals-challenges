
def find_keysize():
    with open('challenge_data_6.txt', 'r') as file:
        ciphertext = base64.b64file.read().strip()

    scored_keysize_values = {}
    for keysize in range(2, 41):
        keysized_blocks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]

