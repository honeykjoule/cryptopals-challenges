def fixed_xor(buffer1: bytes, buffer2: bytes) -> bytes:
    if len(buffer1) != len(buffer2):
        raise ValueError('Both buffers should be of equal length')
    xor_result = bytearray()
    for b1, b2 in zip(buffer1, buffer2):
        xor_result.append(b1 ^ b2)
    return bytes(xor_result)
