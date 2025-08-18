from binascii import unhexlify
from Crypto.Cipher import AES
import string
import re

ciphertext = unhexlify("e2ea0d318af80079fb56db5674ca8c274c5fd0e92019acd01e89171bb889f6b1")

for i in range(4096):
    hex_string = f"{i:03x}"
    
    byte0 = int(hex_string[:2], 16)
    byte1 = (int(hex_string[2], 16) << 4) & 0xFF
    key = bytes([byte0, byte1] + [0] * 14)
    
    cipher = AES.new(key, AES.MODE_CBC, key)
    decrypted = cipher.decrypt(ciphertext)
    
    padding_length = decrypted[-1]
    if padding_length <= 16:
        expected_padding = bytes([padding_length]) * padding_length
        if decrypted[-padding_length:] == expected_padding:
            plaintext = decrypted[:-padding_length]
            
            try:
                text = plaintext.decode('utf-8')
                is_printable = all(ch in string.printable for ch in text)
                has_flag = re.search(r'scriptCTF\{', text)
                
                if is_printable and has_flag:
                    print(text)
                    break
            except:
                continue