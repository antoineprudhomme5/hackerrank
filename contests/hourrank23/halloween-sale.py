p, d, m, s = list(map(int, input().split()))

count = 0

while s >= p and p != m:
    count += 1
    s -= p
    p -= d
    if p < m:
        p = m

count += s // p

print(count)
