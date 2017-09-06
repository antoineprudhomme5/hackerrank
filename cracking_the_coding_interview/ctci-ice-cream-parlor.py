"""
    Do quickSort on an array of flavors, on the price key
"""
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i['price'] < pivot['price']:
                less.append(i)
            elif i['price'] > pivot['price']:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

"""
    go through each flavor, and search the complement flavor
"""
def search_complement(money, flavor, flavors):
    complement_price = money - flavor['price']
    l = 0
    r = len(flavors) - 1
    while r >= l:
        mid = l + (r - l)//2
        if flavors[mid]['price'] == complement_price and flavors[mid]['index'] != flavor['index']:
            return flavors[mid]

        if flavors[mid]['price'] > complement_price:
            r = mid-1
        else:
            l = mid+1

"""
    Given our money and the different flavors,
    search the 2 different flavors which cost our money

    return a string with the indexes separated by a space
"""
def search_flavors(money, flavors):
    for flavor in flavors:
        complement = search_complement(money, flavor, flavors)
        if complement is not None:
            return str(flavor['index']) + " " + str(complement['index']) if complement['index'] > flavor['index'] else str(complement['index']) + " " + str(flavor['index'])
    return ""


# for each test case
for _ in range(int(input().strip())):
    money = int(input().strip())
    nb_flavors = int(input().strip())
    flavors = []

    # store the prices that are lower than our money
    prices = list(map(int, input().strip().split(' ')))
    for i in range(len(prices)):
        if prices[i] < money:
            flavors.append({'index': i + 1, 'price': prices[i]})

    # sort the flavors prices
    flavors = quickSort(flavors)

    # search the 2 flavors
    print(search_flavors(money, flavors))
