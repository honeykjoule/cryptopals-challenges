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
