def fixed_XOR(hex_str_one, hex_str_two):
  hex_pairs_one = [hex_str_one[i:i+2] for i in range(0, len(hex_str_one), 2)]
  hex_pairs_two = [hex_str_two[i:i+2] for i in range(0, len(hex_str_two), 2)]

  integer_list_one = [int(pair, 16) for pair in hex_pairs_one]
  integer_list_two = [int(pair, 16) for pair in hex_pairs_two]

  byte_array_one = bytearray(integer_list_one)
  byte_array_two = bytearray(integer_list_two)

  print(byte_array_one)
  print(byte_array_two)

  assert len(byte_array_one) == len(byte_array_two), 'Unequal buffer lengths'

  hex_str_result = ''

  for i in range (0, len(byte_array_one), 1):
    xor_byte_result = byte_array_one[i] ^ byte_array_two[i]
    hex_result = '{:02x}'.format(xor_byte_result)
    hex_str_result += hex_result
  
  print('Result:', hex_str_result)
  return hex_str_result
      
def run_tests():
  hex_str_one = '1c0111001f010100061a024b53535009181c'
  hex_str_two = '686974207468652062756c6c277320657965'
  expected_result = '746865206b696420646f6e277420706c6179'
  test_cases = [
    (hex_str_one, hex_str_two, expected_result)
  ]

  for i, (hex_str_one, hex_str_two, expected_result), in enumerate(test_cases):
    result = fixed_XOR(hex_str_one, hex_str_two)
    success = result == expected_result
    print(f"Test{i}: {'Success' if success else 'Failure'}")

if __name__ == "__main__":
  run_tests()
