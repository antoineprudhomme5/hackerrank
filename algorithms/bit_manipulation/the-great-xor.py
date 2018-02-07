#!/bin/python3

import sys

def bit_length(x):
    i = 0
    while x > 0:
        i += 1
        x >>= 1
    return i

def the_great_xor(x):
    # calculate the length in bit of x
    length = bit_length(x)
    return (1 << length) - 1 - x

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    result = the_great_xor(x)
    print(result)
