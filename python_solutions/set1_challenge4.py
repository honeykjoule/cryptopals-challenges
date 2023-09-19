from utilities.conversions import convert_hex_to_bytes
from utilities.xor_operations import single_byte_xor
from utilities.frequency_analysis import score_text_etaoin_shrdlu

def main():
    best_key = None
    best_score = 0
    best_decrypted_line = ''
    line_number = 0
    with open('challenge_data/set1_challenge4.txt', 'r') as file:
        for line in file:
            line_number += 1
            line = line.strip()
            line_bytes = convert_hex_to_bytes(line)

            best_byte_score = 0
            best_byte_key = None
            best_decryption = ''

            for key in range(256):
                xor_byte_result = single_byte_xor(line_bytes, key)
                try:
                    plaintext_result = xor_byte_result.decode('utf-8')
                except UnicodeDecodeError:
                    continue

                current_byte_score = score_text_etaoin_shrdlu(plaintext_result)
                if current_byte_score > best_score:
                    best_byte_score = current_byte_score
                    best_byte_key = key
                    best_decryption = plaintext_result
            
            if best_byte_score > best_score:
                best_score =  best_byte_score
                best_decrypted_line = best_decryption
                best_key = best_byte_key

    print(f"decryption: {best_decrypted_line}, key: {best_key}")

if __name__ == "__main__":
    main()
