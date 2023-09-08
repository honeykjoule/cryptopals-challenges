def convert_base64_to_bytes(base64_str):
    base64_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    complete_binary_str = ''
    padding_count = base64_str.count('=')
    base64_str = base64_str.rstrip('=')

    for char in base64_str:
        index = base64_alphabet.index(char)
        binary_representation = bin(index)[2:].zfill(6)
        complete_binary_str += binary_representation

    remaining_bits = len(complete_binary_str) % 8
    if remaining_bits:
        complete_binary_str = complete_binary_str[:-remaining_bits]
    
    byte_chunks = [complete_binary_str[i:i+8] for i in range(0, len(complete_binary_str), 8)]
    byte_values = [int(chunk, 2) for chunk in byte_chunks]
    return bytes(byte_values)

def run_tests():
    base64_str = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    expected_bytes = b"I'm killing your brain like a poisonous mushroom"
    
    base64_str_two_bytes = "TWE="
    expected_bytes_two_bytes = b"Ma"

    base64_str_one_byte = "TQ=="
    expected_bytes_one_byte = b"M"

    test_cases = [
        (base64_str, expected_bytes),
        (base64_str_two_bytes, expected_bytes_two_bytes),
        (base64_str_one_byte, expected_bytes_one_byte)
    ]

    for i, (input_base64, expected_bytes) in enumerate(test_cases):
        result = convert_base64_to_bytes(input_base64)
        success = result == expected_bytes
        print(f"Test{i+1}: {'Success' if success else 'Failure'}")

if __name__ == '__main__':
    run_tests()
