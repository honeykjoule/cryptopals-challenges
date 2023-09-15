from utilities.conversions import convert_hex_to_bytes
from utilities.xor_operations import single_byte_xor
from utilities.frequency_analysis import score_text

def main():
    hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    frequency_table = {}
    for index, char in enumerate('ETAOIN SHRDLU'):
        frequency_table[char] = 12 - index

    byte_data = convert_hex_to_bytes(hex_str)

    best_score = 0
    best_key = None
    best_decryption = ''

    for key in range(256):
        decrypted_bytes = single_byte_xor(byte_data, key)
        decrypted_text = decrypted_bytes.decode('utf-8', errors='replace')

        current_score = score_text(decrypted_text, frequency_table)
        if current_score > best_score:
            best_score =  current_score
            best_key = key
            best_decryption = decrypted_text

    print(f"Challenge completed: best key is {best_key}")
    print(f"Best decryption: {best_decryption}")

if __name__ == "__main__":
    main()
