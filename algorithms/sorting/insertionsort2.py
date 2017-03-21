n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    j = i
    v = a[i]
    while j > 0 and a[j - 1] > v:
         a[j] = a[j-1]
         j -= 1
    a[j] = v

    print(' '.join(str(v) for v in a))