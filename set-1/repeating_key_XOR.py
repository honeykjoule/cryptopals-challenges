def repeating_key_XOR(text, key):
  text_byte_array = text.encode('utf8')
  key_byte_array = key.encode('utf8')
  hex_output = ''

  for i, byte in enumerate(text_byte_array):
    key_index = i % len(key_byte_array)
    encrypted_byte = byte ^ key_byte_array[key_index]
    hex_output += '{:02x}'.format(encrypted_byte)

  return hex_output

def run_tests():
  text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
  key = 'ICE'
  expected_output = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
  test_cases = [(text, key, expected_output)]

  for i, (text, key, expected_output) in enumerate(test_cases):
    result = repeating_key_XOR(text, key)
    success = result == expected_output
    print(f"Test{i}: {'Success' if success else 'Failure'}")

if __name__ == '__main__':
  run_tests()
