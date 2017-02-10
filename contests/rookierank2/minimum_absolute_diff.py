import math

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = 100000000
for i in range(n-1):
    t = math.fabs(a[i] - a[i+1])
    if t < m:
        m = t
        if m < 1:
            break
print(int(m))