a = list(map(int, input().split()))
a.sort()
print('%d %d' % (sum(a[:len(a)-1]), sum(a[1:])))