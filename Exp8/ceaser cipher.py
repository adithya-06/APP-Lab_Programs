def cipher(c):
    if c.isalpha():
        if c.isupper():
            return chr((ord(c) + 3 - 65) % 26 + 65)
        return chr((ord(c) + 3 - 97) % 26 + 97)
    return c

print(''.join(map(cipher,input())))

