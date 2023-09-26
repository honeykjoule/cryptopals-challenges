def galois_field_multiplication(a, b):
    p = 0
    while b:
        if b & 1:
            p ^= a
        a <<=1
        if a & 0x100:
            a ^= 0x11b
        b >>= 1
    return p & 0xff

def galois_field_inverse(a):
    for i in range(256):
        if galois_field_multiplication(a, i) == 1:
            return i
    return 0

def affine_transformation(b):
    b = b ^ (b << 1) ^ (b << 2) ^ (b << 3) ^ (b << 4)
    return (b & 0xff) ^ 0x63

def generate_rcon():
    RCON = [0]
    rcon_val = 1
    for _ in range(1, 32):
        RCON.append(rcon_val)
        rcon_val = galois_field_multiplication(rcon_val, 0x02)
    return RCON
