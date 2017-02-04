import math

n = int(input())
a = list(map(int, input().split()))

m = -1

for i in range(n):
    for j in range(i+1, n):
        if a[i] == a[j]:
            v_abs = math.fabs(i-j)
            if m == -1 or v_abs < m:
                m = v_abs

print(int(m))