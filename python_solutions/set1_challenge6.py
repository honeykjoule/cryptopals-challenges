from utilities.conversions import convert_base64_to_bytes
from utilities.find_keysize import find_keysize, find_repeating_key
from utilities.xor_operations import repeating_key_xor

def main():
    with open('challenge_data/set1_challenge6.txt', 'r') as file:
        ciphertext_base64 = file.read().strip().replace('\n', '')
    
    cipher_text = convert_base64_to_bytes(ciphertext_base64)
    keysize = find_keysize(cipher_text)
    key = find_repeating_key(cipher_text, keysize)
    decrypted_text = repeating_key_xor(cipher_text, key)

    print(f"found key: {key.decode('utf-8')}")
    print(f"decrypted_text: {decrypted_text.decode('utf-8')}")

if __name__ == "__main__":
    main()
