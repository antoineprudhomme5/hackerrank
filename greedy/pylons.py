#!/bin/python3

import sys

def pylons(n, k, arr):
    min_tower = 0

    last_tower_i = 0
    i = 0
    while i < n:
        j = min(n-1, i+k-1)
        while j >= last_tower_i and arr[j] == 0:
            j -= 1
        if j < last_tower_i:
            return -1
        else:
            last_tower_i = j+1
            min_tower += 1
            i = j+k

    return min_tower

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().strip().split(' ')))
    print(pylons(n, k, arr))
