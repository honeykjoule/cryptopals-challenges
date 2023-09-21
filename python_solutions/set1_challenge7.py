from utilities.conversions import convert_base64_to_bytes
from utilities.aes_encryption import decrypt_aes_ecb

def main():
    KEY = b'YELLOW SUBMARINE'

    with open('challenge_data/set1_challenge7', 'r') as file:
        base64_data = file.read().replace('\n', '')
        ciphertext = convert_base64_to_bytes(base64_data)

    decrypted_text = decrypt_aes_ecb(ciphertext, KEY)
        
    print(decrypted_text.decode('utf-8'))

if __name__ == "__main__":
    main()
