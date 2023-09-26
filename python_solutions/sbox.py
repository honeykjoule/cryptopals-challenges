from utilities.aes_encryption import affine_transformation, galois_field_inverse

s_box =  [affine_transformation(galois_field_inverse(i)) for i in range(256)]

inverse_s_box = [0] * 256
for i in range(256):
    inverse_s_box[s_box[i]] = i

print("S-Box:", s_box)
print("Inverse S-Box:", inverse_s_box)
