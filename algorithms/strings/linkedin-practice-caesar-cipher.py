import string

def rotate_alphabet(k):
    alphabet = list(string.ascii_lowercase)
    rotated_alphabet = {}

    for i in range(len(alphabet)):
        rotated_alphabet[alphabet[i]] = alphabet[(i+k) % len(alphabet)]

    return rotated_alphabet

def encrypt(c, alphabet):
    upper = c.isupper()
    c = c.lower()
    if c not in alphabet:
        return c
    return alphabet[c].upper() if upper else alphabet[c]

l = int(input())
s = list(input())
k = int(input())

encrypt_alphabet = rotate_alphabet(k)
print(''.join([encrypt(c, encrypt_alphabet) for c in s]))
