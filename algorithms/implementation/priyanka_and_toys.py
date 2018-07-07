n = int(input())
a = sorted(list(map(int, input().split())))

c = 1
start = 0
for current in range(1, n):
	if a[current] - a[start] > 4:
		start = current
		c += 1
print(c)