line_number = 0
best_line_number = 0
best_key = None
best_score = 0
best_line = ''
best_encrypted_line = ''
filename = 'set_one/challenge_data_4.txt'


def score_text(text, frequency_table):
  score = 0

  for char in text.upper():
    score += frequency_table.get(char, 0)
  return score


with open(filename, 'r') as file:
  for line in file:
    line_number += 1
    line = line.strip()
    encrypted_line = line

    frequency_table = {}
    for index, char in enumerate('ETAOIN SHDRLU'):
      frequency_table[char] = 12 - index

    hex_pairs = [line[i:i+2] for i in range(0, len(line), 2)]
    integer_list = [int(pair, 16) for pair in hex_pairs]
    byte_array = bytearray(integer_list)

    best_byte_score = 0
    best_byte_key = None
    best_decryption = ''

    for key in range(256):
      plaintext_result = ''

      for byte in byte_array:
        xor_byte_result = key ^ byte
        plaintext_result += chr(xor_byte_result)

        current_byte_score = score_text(plaintext_result, frequency_table)
        if current_byte_score > best_score:
          best_byte_score = current_byte_score
          best_byte_key = key
          best_decryption = plaintext_result

    if best_byte_score > best_score:
      best_score = best_byte_score
      best_line = best_decryption
      best_line_number = line_number
      best_encrypted_line = encrypted_line
      best_key = best_byte_key

print(f"line number: {best_line_number}, line: {best_line}, key: {best_key}, encrypted line: {best_encrypted_line}")
