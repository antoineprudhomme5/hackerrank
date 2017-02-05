import string 

n = int(input().strip())
s = list(input().strip())
k = int(input().strip()) % 26


for i in range(len(s)):
    ascii_v = ord(s[i])
    # if lower case char
    if ascii_v >= 97 and ascii_v <= 122:
        ascii_v += k
        if ascii_v > 122:
            ascii_v -= 26
        s[i] = chr(ascii_v)
    # if upper case char
    if ascii_v >= 65 and ascii_v <= 90:
        ascii_v += k
        if ascii_v > 90:
            ascii_v -= 26
        s[i] = chr(ascii_v)

print(''.join(s))