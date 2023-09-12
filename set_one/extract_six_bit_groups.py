
def extract_six_bit_groups(three_bytes):
    print(f"Three bytes in binary: {format(three_bytes[0], '08b')} {format(three_bytes[1], '08b')} {format(three_bytes[2], '08b')}")

    first_six_bits = (three_bytes[0] & 0xFC) >> 2
    print(f"First six bits: {format(first_six_bits, '06b')}")

    second_six_bits = ((three_bytes[0] & 0x03) << 4) | (three_bytes[1] >> 4)
    print(f"Second six bits: {format(second_six_bits, '06b')}")

    third_six_bits = ((three_bytes[1] & 0x0F) << 2) | (three_bytes[2] >> 6)
    print(f"Third six bits: {format(third_six_bits, '06b')}")

    fourth_six_bits = three_bytes[2] & 0x3F
    print(f"Fourth six bits: {format(fourth_six_bits, '06b')}")

    return [first_six_bits, second_six_bits, third_six_bits, fourth_six_bits]

three_bytes_example = [0x48, 0x65, 0x6C]  # Example bytes for 'Hel'
extract_six_bit_groups(three_bytes_example)
