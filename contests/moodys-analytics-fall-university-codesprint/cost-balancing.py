from math import floor

n, m = map(int, input().split())
spendings = [0] * (m+1)

for _ in range(n):
    i, amount = map(int, input().split())
    spendings[i] += amount

total = sum(spendings)
part = floor(total / m)

# Anita (with extra)
print("1 %d" % ((total - (m-1) * part - spendings[1]) * -1))

# his friends
for i in range(2, m+1):
    print("%d %d" % (i, spendings[i] - part))
