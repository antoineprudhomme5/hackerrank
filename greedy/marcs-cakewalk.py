#!/bin/python3

n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))

calories = sorted(calories, reverse=True)

print(sum([(cal*(2**j)) for j, cal in enumerate(calories)]))
