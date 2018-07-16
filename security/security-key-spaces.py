n = list(input())
e = int(input())
for i in range(len(n)):
    n[i] = str((int(n[i]) + e) % 10)
print(''.join(n))