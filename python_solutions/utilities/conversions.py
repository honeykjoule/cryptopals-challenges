def convert_hex_to_bytes(hex_string: str) -> bytes:
    byte_array = bytearray()
    for i in range(0, len(hex_string), 2):
        byte = int(hex_string[i:i+2], 16)
        byte_array.append(byte)
    return bytes(byte_array)

def convert_bytes_to_base64(byte_data: bytes) -> str:
    base64_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    base64_string = ''
    
    original_length = len(byte_data)
    
    padding = len(byte_data) % 3
    if padding:
        byte_data += b'\x00' * (3 - padding)
    
    for i in range(0, len(byte_data), 3):
        chunk = byte_data[i:i+3]

        twenty_four_bit = (chunk[0] << 16) + (chunk[1] << 8) + chunk[2]

        indices = [
                (twenty_four_bit >> 18) & 0x3F,
                (twenty_four_bit >> 12) & 0x3F,
                (twenty_four_bit >> 6) & 0x3F,
                twenty_four_bit & 0x3F
        ]

        for index in indices:
            base64_string += base64_alphabet[index]

        if padding:
            padding_chars = 3 - original_length % 3
            base64_string = base64_string[:-padding_chars] + '=' * padding_chars
        
    return base64_string

def convert_base64_to_bytes(base64_string: str) -> bytes:
    base64_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    base64_dict = {char: index for index, char in enumerate(base64_alphabet)}
    complete_binary_list = []
    padding_length = base64_string.count('=')
    base64_string = base64_string.strip('=')

    for char in base64_string:
        binary_representation = bin(base64_dict[char])[2:].zfill(6)
        complete_binary_list.append(binary_representation)

    complete_binary_str = ''.join(complete_binary_list)
    if padding_length:
        complete_binary_str = complete_binary_str[:-(padding_length * 2)]

    byte_chunks = [
        complete_binary_str[i:i+8] 
        for i in range(0, len(complete_binary_str), 8)
    ]
    byte_values = [int(chunk, 2) for chunk in byte_chunks]

    return bytes(byte_values)
