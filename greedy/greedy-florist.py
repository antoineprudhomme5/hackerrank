n, k = map(int, input().split())
prices = sorted(list(map(int, input().split())), reverse=True)

cost = 0
rnd = 0

for i, price in enumerate(prices):
    if i % k == 0:
        rnd += 1

    cost += rnd * price

print(cost)
