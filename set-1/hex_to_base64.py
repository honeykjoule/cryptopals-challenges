hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base64_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def hex_to_base64(hex_str):

  print('hex_str:', hex_str)
  
  hex_pairs = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
  print('hex_pairs:', hex_pairs)

  integer_list = [int(pair, 16) for pair in hex_pairs]
  print('integer_list:', integer_list)

  byte_array = bytearray(integer_list)
  print('byte_array:', byte_array)

  three_byte_list = []

  for i in range(0, len(byte_array), 3):
    three_bytes = byte_array[i:i+3]
    print('three bytes:', three_bytes)

    three_byte_list.append(three_bytes)
  
  print('three_byte_list:', three_byte_list)
  
  return byte_array

hex_to_base64(hex_str)
