import math

s = input()
len_s = len(s)
root = math.sqrt(len_s)

rows = math.floor(root)
cols = math.ceil(root)

if (rows * cols) < len_s:
    rows += 1

p = ''

for i in range(cols):
    for j in range(rows):
        if ((j)*cols + i) < len_s:
            p += s[(j)*cols + i]
    p += ' '

print(p)
