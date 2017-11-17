n, m, k = map(int, input().split())

a = [[0]*n for _ in range(n)]
a[0][0] = m

for i in range(n):
    for j in range(n):
        if i == j and (j != 0 or i != 0):
            a[i][j] = a[i-1][j-1] + k
        elif i > j:
            a[i][j] = a[i-1][j] - 1
        elif j > i:
            a[i][j] = a[i][j-1] - 1

for i in range(n):
    print(' '.join([str(v) for v in a[i]]))
