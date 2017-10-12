# number of days
n = int(input())
# read prices of all days
days_prices = list(map(int, input().split()))
# search the lower price
min_price = min(days_prices)

# from days prices, remember only the last index of each price
prices_dic = {}
for i in range(n):
    prices_dic[days_prices[i]] = i
# get all discinct prices (keys of the prices_dic)
prices = list(prices_dic.keys())

# reverse the prices_dic (indexes are now the keys)
indexes_dic = {v: k for k, v in prices_dic.items()}
# get all the indexes and sort them => we want the last day the customer can buy
# so we need to find the biggest index where the price is <= than his price
indexes = sorted(indexes_dic.keys())

# handle customers queries
for _ in range(int(input())):
    # read the price of the customer
    price = int(input())
    # default value = -1 (when it's impossible)
    last_day = -1

    # search only if his price his >= than the lowest stock price
    if price >= min_price:
        # loop in decreasing order (indexes are sorted)
        for i in range(len(indexes)-1, -1, -1):
            if indexes_dic[indexes[i]] <= price:
                last_day = indexes[i] + 1
                break

    # print the last day he can buy stock
    print(last_day)
