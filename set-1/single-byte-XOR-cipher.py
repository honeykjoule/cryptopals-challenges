def score_text(text, frequency_table):
  score = 0
  
  for char in text.upper():
    score += frequency_table.get(char, 0)
  return score
    
  

def single_byte_XOR_cipher(hex_str):
  
  frequency_table = {}
  for index, char in enumerate('ETAOIN SHRDLU'):
    frequency_table[char] = 12 - index

  hex_pairs = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
  integer_list = [int(pair, 16) for pair in hex_pairs]
  byte_array = bytearray(integer_list)
  
  best_score = 0
  best_key = None
  best_decryption = ''

  for key in range(256):
    plaintext_result = ''

    for byte in byte_array:
      xor_byte_result = key ^ byte
      plaintext_result += chr(xor_byte_result)
    
    current_score = score_text(plaintext_result, frequency_table)
    if current_score > best_score:
      best_score = current_score
      best_key = key
      best_decryption = plaintext_result
  
  print('key:', best_key, 'decryption:', best_decryption, 'score:', best_score)
  return best_key
      
    
hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

if __name__ == "__main__":
  single_byte_XOR_cipher(hex_str)
