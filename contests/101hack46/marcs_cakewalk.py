n = int(input())
c = list(map(int, input().split()))
c.sort(reverse=True)

miles = 0

for i in range(n):
    miles += c[i] * 2**i

print(miles)
