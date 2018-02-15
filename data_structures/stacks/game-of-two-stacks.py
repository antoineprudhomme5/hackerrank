#!/bin/python3

import sys

for _ in range(int(input())):
    n, m, x = map(int, input().split())
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))

    # down the stack 'a' as far as possible
    s = 0
    i = 0
    while i < n and (s+a[i]) <= x :
        s += a[i]
        i += 1

    # set current max
    curr_max = i

    # expand in stack 'b' and update curr_max if current situation is better
    j = 0
    while j < m and i >= 0:
        s += b[j]
        j += 1
        while s > x and i > 0:
            i -= 1
            s -= a[i]
        if s <= x:
            curr_max = max(curr_max, i+j)

    print(curr_max)
