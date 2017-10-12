n = int(input())

prices_dic = {}
days_prices = list(map(int, input().split()))
for i in range(n):
    # if the price exist => update index
    # else, add the new price
    prices_dic[days_prices[i]] = i
prices = list(prices_dic.keys())

indexes_dic = {v: k for k, v in prices_dic.items()}
indexes = sorted(indexes_dic.keys())

# handle customers
for _ in range(int(input())):
    price = int(input())
    flag = -2
    for i in range(len(indexes)-1, -1, -1):
        if indexes_dic[indexes[i]] <= price:
            flag = indexes[i]
            break
    print(flag + 1)
