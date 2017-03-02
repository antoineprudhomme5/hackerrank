m, n = list(map(int, input().split()))
for _ in range(n):
    a, b = list(map(int, input().split()))
    if a == m:
        m = b
    elif b == m:
        m = a
print(m)
