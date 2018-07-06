p, d, m, s = list(map(int, input().split()))

c = 0
while s - p >= 0:
    c += 1
    s -= p
    p = max(m, p-d)
print(c)