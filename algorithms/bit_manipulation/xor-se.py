#!/bin/python3

import sys

def val(i):
    # we can get the value at index i in O(1), because of the pattern
    if i%4 == 0: return i
    if i%4 == 1: return 1
    if i%4 == 2: return i+1
    if i%4 == 3: return 0

def solve(L, R):
    r = 0
    # ignore blocks of length 8 starting at index i
    # such as i%8 == 0, because XOR all the elements = 0
    while (L+1)%8 != 0 and R >= L:
        r ^= val(L)
        L += 1
    if R > L:
        while (R+1)%8 != 0:
            r ^= val(R)
            R -= 1
    return r

for _ in range(int(input())):
    L, R = map(int, input().split())
    print(solve(L, R))
