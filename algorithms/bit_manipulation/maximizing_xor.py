l, r = int(input()), int(input())
max = 0
for a in range(l, r+1):
    for b in range(a, r+1):
        xor = a^b
        if xor > max:
            max = xor
print(max)
