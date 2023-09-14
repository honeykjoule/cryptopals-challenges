from utilities.conversions import convert_hex_to_bytes, convert_bytes_to_base64

def main():
    given_hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected_base64_string = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    bytes_data = convert_hex_to_bytes(given_hex_string)
    base64_string = convert_bytes_to_base64(bytes_data)
    success = (base64_string == expected_base64_string)

    print(f"Challenge Succesful: {success}")

if __name__ == "__main__":
    main()
