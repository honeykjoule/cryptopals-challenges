def single_byte_XOR_cipher(hex_str):

  hex_pairs = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
  integer_list = [int(pair, 16) for pair in hex_pairs]
  byte_array = bytearray(integer_list)


  for i in range(0, 255):

    cipher = byte(i)
    plaintext_result = ''


    for i in 
