n = int(input())
d = {}
for i in input().split():
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i, c in d.items():
    if c == 1:
        print(i)
        break
