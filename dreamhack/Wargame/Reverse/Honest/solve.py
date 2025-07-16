def calculate(a1: int) -> int:
    temp_calc = (4 * (a1 ^ 0x3C)) | (((a1 ^ 0x3C) & 0xFF) >> 6)
    v1 = 32 * ((5 * temp_calc + 125) & 0xFF)
    v1 &= 0xFFFF
    hibyte_v1 = (v1 >> 8) & 0xFF
    tmp = (hibyte_v1 | (v1 & 0xFF)) & 0xFF
    temp_xor = tmp ^ 0xB2
    v3 = (3 * ((16 * temp_xor) | ((temp_xor >> 4) & 0xFF)) - 47) & 0xFF
    v4 = ((2 * v3) | (v3 >> 7)) ^ 0xD4
    v4 &= 0xFF
    v5 = 0
    for i in range(8):
        v5 = (2 * v5) | (v4 & 1)
        v4 >>= 1
    return v5

reverse_mapping = {}
for c in "abcdefghijklmnopqrstuvwxyz1234567890":
    reverse_mapping[calculate(ord(c))] = c

lst = [189, 177, 59, 101, 151, 238, 189, 183,
       205, 151, 185, 177, 238, 202, 227, 177,
       25, 101, 195, 183, 193, 227, 59, 232,
       183, 185, 59, 185, 98, 232, 189, 183,
       185, 101, 205, 185, 25, 193, 59, 205,
       177, 183, 195, 238, 193, 195, 238, 183,
       202, 232, 195, 193, 177, 59, 25, 238,
       205, 232, 151, 189, 205, 101, 98, 101]

flag = ""
for i in lst:
    flag += reverse_mapping[i]

print("Key: " + flag)
print("Flag: DH{" + flag + "}")