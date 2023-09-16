from utilities.xor_operations import repeating_key_xor, convert_bytes_to_hex

def main():
    text_bytes = (
        b"Burning 'em, if you ain't quick and nimble\n"
        b"I go crazy when I hear a cymbal"
    )
    key_bytes = b'ICE'
    expected_output = (
        "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
        "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    )

    encrypted_bytes = repeating_key_xor(text_bytes, key_bytes)
    result = convert_bytes_to_hex(encrypted_bytes)
    success = result == expected_output
    
    print(f"Result: {'Success' if success else 'Failure'}")

    return expected_output, success

if __name__ == "__main__":
    main()
