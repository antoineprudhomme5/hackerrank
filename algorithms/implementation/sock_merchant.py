n = int(input())
d = {}
for s in input().split():
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
pairs = 0
for k, v in d.items():
    pairs += v // 2
print(pairs)