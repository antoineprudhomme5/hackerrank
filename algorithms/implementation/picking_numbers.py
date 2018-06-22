n = int(input())
a = list(map(int, input().split()))

d = {}
for v in a:
	if v in d:
		d[v] += 1
	else:
		d[v] = 1

m = float('-Inf')
for k, _ in d.items():
	if (k-1) in d:
		tmp = d[k] + d[k-1]
		m = max(m, tmp)
	if (k+1) in d:
		tmp = d[k] + d[k+1]
		m = max(m, tmp)
	m = max(m, d[k])
print(m)