# 2 levels memoization : first is the amount of money,
# second is the current coin's index
memo = {}

def make_change(coins, money, index = 0):
    if money == 0:
        return 1
    if index >= len(coins):
        return 0

    amount = 0
    ways = 0

    if money not in memo:
        memo[money] = {}

    if index not in memo[money]:
        while amount <= money:
            remaining = money - amount
            ways += make_change(coins, remaining, index + 1)
            amount += coins[index]
        memo[money][index] = ways

    return memo[money][index]

money, nb_coins = list(map(int, input().split()))
coins = list(map(int, input().split()))
print(make_change(coins, money))
