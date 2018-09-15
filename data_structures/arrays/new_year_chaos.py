#!/bin/python3
def minimumBribes(a):
    count = 0
    for i in range(len(a)):
        if a[i]-i-1 > 2:
            return -1
        for j in range(max(0, a[i]-3), i):
            if a[j] > a[i]:
                count += 1
    return count

for _ in range(int(input())):
    input()
    a = list(map(int, input().rstrip().split()))
    r = minimumBribes(a)
    print("Too chaotic" if r == -1 else r)