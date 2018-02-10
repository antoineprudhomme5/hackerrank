#!/bin/python3

import sys

def angryChildren(k, arr):
    arr.sort()
    min_unfairness = float("Inf")
    for i in range(len(arr)-k+1):
        min_unfairness = min(arr[i+k-1] - arr[i], min_unfairness)
    return min_unfairness

if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
       arr.append(int(input().strip()))
    print(angryChildren(k, arr))
