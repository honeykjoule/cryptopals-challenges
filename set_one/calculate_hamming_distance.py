def calculate_hamming_distance(string_one, string_two):
    if isinstance(string_one, str):
        string_one = string_one.encode()
    if isinstance(string_two, str):
        string_two = string_two.encode()

    paired_elements = zip(string_one, string_two)
    xor_results = [a ^ b for a, b in paired_elements]
    hamming_distance = sum(bin(x).count('1') for x in xor_results)
    return hamming_distance

def test_calculate_hamming_distance():
    string_one = 'this is a test'
    string_two = 'wokka wokka!!!'
    expected_hamming_distance = 37

    test_cases = [
            (string_one, string_two, expected_hamming_distance),
            (string_one.encode(), string_two.encode(), expected_hamming_distance)
    ]

    for i, (string_one, string_two, expected_hamming_distance) in enumerate(test_cases):
        hamming_distance = calculate_hamming_distance(string_one, string_two)
        success = hamming_distance == expected_hamming_distance
        print(f"Test{i}: {'Success' if success else 'Failure'}")
      

if __name__ == '__main__':
    test_calculate_hamming_distance()
