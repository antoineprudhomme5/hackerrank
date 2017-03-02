n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
d = {}
# insane brute force solution ...
for i in range(n+1):
    for j in range(n+1):
        sub = a[i:j]
        if len(sub):
            diff = max(sub) - min(sub)
            if diff in d:
                d[diff] += 1
            else:
                d[diff] = 1
keys = list(d.keys())
keys.sort()
# for each query
for _ in range(q):
    pairs = 0
    low, high = list(map(int, input().split()))
    for k in keys:
        if k >= low and k <= high:
            pairs += d[k]
    print(pairs)
