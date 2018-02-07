#!/bin/python3

import sys

def next_power_of_two(v):
    i = 0
    # shift while != 0 to get the MSB
    while v != 0:
        v >>= 1
        i += 1
    return 1 << i

def and_product(a, b):
    # keep only the leftmost aligned bits
    mask = ~(next_power_of_two(a^b) - 1)
    return a & mask

if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = and_product(a, b)
        print(result)
