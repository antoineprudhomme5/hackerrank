#!/bin/python3

def lonely_integer(a):
    v = 0
    for i in a:
        v ^= i
    return v

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
