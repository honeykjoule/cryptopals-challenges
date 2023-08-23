def single_byte_XOR_cipher(hex_str):

  hex_pairs = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
  integer_list = [int(pair, 16) for pair in hex_pairs]
  byte_array = bytearray(integer_list)


  for key in range(256):
    plaintext_result = ''

    for byte in byte_array:
      xor_byte_result = key ^ byte
      plaintext_result += chr(xor_byte_result)

    print(plaintext_result)

hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
single_byte_XOR_cipher(hex_str)
