#!/bin/python3

import sys

def pairs(k, arr):
    dic = {}
    for v in arr:
        dic[v] = True

    pairs_count = 0
    for v in arr:
        if (v+k) in dic:
            pairs_count += 1

    return pairs_count

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pairs(k, arr)
    print(result)
