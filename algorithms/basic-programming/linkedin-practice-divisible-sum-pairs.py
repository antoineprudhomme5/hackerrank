n, k = map(int, input().split())
a = list(map(int, input().split()))

c = 0
for j in range(1, n):
    for i in range(j):
        if (a[i] + a[j]) % k == 0:
            c += 1
print(c)
