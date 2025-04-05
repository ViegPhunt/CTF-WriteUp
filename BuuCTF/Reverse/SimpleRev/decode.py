alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

text = "killshadow"
key = "adsfkndcls"
v3 = v5 = len(key)
strres = ""

for i in range(10):
    for i in alphabet:
        temp = chr((ord(i) - 39 - ord(key[v3 % v5]) + 97) % 26 + 97)
        if (temp == text[len(strres)]):
            strres += i
            v3 += 1
            break

print(strres)