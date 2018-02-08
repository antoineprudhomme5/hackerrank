#!/bin/python3

import sys

def cipher(n, k, s):
    answer = [0 for _ in range(n)]
    acc = 0

    for i in range(n):
        if i >= k:
            acc ^= answer[i-k]
        if acc == s[i]:
            answer[i] = 0
        else:
            answer[i] = 1
        acc ^= answer[i]

    return ''.join(map(str, answer))

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = [int(c) for c in input()]
    print(cipher(n, k, s))
