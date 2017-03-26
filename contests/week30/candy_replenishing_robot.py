n, t = list(map(int, input().split()))
c = list(map(int, input().split()))
bowl = n
added = 0
for i in range(t-1):
    bowl -= c[i]
    if bowl < 5:
        added += n - bowl
        bowl = n
print(added)