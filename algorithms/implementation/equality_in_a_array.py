n = int(input())
a = input().split()
d = {}

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

m = a[0]
for k, v in d.items():
    if v > d[m]:
        m = k
print(n - d[m])