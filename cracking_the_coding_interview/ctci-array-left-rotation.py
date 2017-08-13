n, d = list(map(int, input().split()))
a = input().split()
l = a[d:] + a[:d]
print(' '.join(l))
