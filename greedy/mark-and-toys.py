#!/bin/python3

import sys

def maximum_toys(n, money, prices):
    prices.sort()
    counter = 0
    for i in range(n):
        money -= prices[i]
        if money < 0:
            break
        else:
            counter += 1
    return counter

if __name__ == "__main__":
    n, k = map(int, input().split())
    prices = list(map(int, input().strip().split(' ')))
    print(maximum_toys(n, k, prices))
