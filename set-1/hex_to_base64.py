
def hex_to_base64(hex_str):

  hex_pairs = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]

  integer_list = [int(pair, 16) for pair in hex_pairs]

  byte_array = bytearray(integer_list)

  base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  base64_result = ''

  for i in range(0, len(byte_array), 3):

    three_bytes = byte_array[i:i+3]
    byte_length = len(three_bytes)

    if byte_length == 2:
      first_six_bits = (three_bytes[0] & 0xFC) >> 2
      second_six_bits = (three_bytes[0] & 0x03) << 4 | (three_bytes[1] >> 4) 
      third_six_bits = (three_bytes[1] & 0x0F) << 2

      base64_result += base64_alphabet[first_six_bits]
      base64_result += base64_alphabet[second_six_bits]
      base64_result += base64_alphabet[third_six_bits]
      base64_result += '='

    elif byte_length == 1:
      first_six_bits = (three_bytes[0] & 0xFC) >> 2
      second_six_bits = (three_bytes[0] & 0x03) << 4 

      base64_result += base64_alphabet[first_six_bits]
      base64_result += base64_alphabet[second_six_bits]
      base64_result += '=='
      
    else:
      first_six_bits = (three_bytes[0] & 0xFC) >> 2
      second_six_bits = (three_bytes[0] & 0x03) << 4 | (three_bytes[1] >> 4) 
      third_six_bits = (three_bytes[1] & 0x0F) << 2 | (three_bytes[2] >> 6)
      fourth_six_bits = three_bytes[2] & 0x3F
        
      base64_result += base64_alphabet[first_six_bits]
      base64_result += base64_alphabet[second_six_bits]
      base64_result += base64_alphabet[third_six_bits]
      base64_result += base64_alphabet[fourth_six_bits]
    
  print('hex input:', hex_str)
  print('base64 result:', base64_result)
  return base64_result

def run_tests():
  
  hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
  base64_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

  hex_str_two_bytes = "4d61"
  base64_str_two_bytes = "TWE="

  hex_str_one_byte = "4d"
  base64_str_one_byte = "TQ=="
  
  test_cases = [
    (hex_str, base64_str),
    (hex_str_two_bytes, base64_str_two_bytes),
    (hex_str_one_byte, base64_str_one_byte)
  ]

  for i, (input_hex, expected_base64), in enumerate(test_cases):
    result = hex_to_base64(input_hex)
    success = result == expected_base64
    print(f"Test{i}: {'Success' if success else 'Failure'}")
    
if __name__ == '__main__':
  run_tests()
