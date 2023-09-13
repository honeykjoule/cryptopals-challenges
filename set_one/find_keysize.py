from calculate_hamming_distance import calculate_hamming_distance
from convert_base64_to_bytes import convert_base64_to_bytes

def find_keysize():
    with open('challenge_data_6.txt', 'r') as file:
        ciphertext_base64 = file.read().strip().replace('\n', '')
        ciphertext = convert_base64_to_bytes(ciphertext_base64)
        if ciphertext is None:
            print('Error converting base64 to bytes')

    scored_keysize_values = {}
    for keysize in range(2, 41):
        keysized_blocks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]

        cumulative_hamming_distance = 0
        number_of_blocks = 0
        for i in range(len(keysized_blocks) -1):
            for j in range(i+1, len(keysized_blocks)):
                cumulative_hamming_distance += calculate_hamming_distance(keysized_blocks[i], keysized_blocks[j])
                number_of_blocks += 1

        scored_keysize_values[keysize] = (cumulative_hamming_distance / number_of_blocks) / keysize


    if not scored_keysize_values:
        print('No scored key sizes')
        return None

    best_keysize = min(scored_keysize_values, key=scored_keysize_values.get)
    print(best_keysize)

    return best_keysize

if __name__ == '__main__':
    find_keysize()
