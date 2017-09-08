import math

input() # ignore the first input
v = sorted(list(map(int, input().split())))

diff = math.inf
# find the min diff between 2 values
for i in range(1, len(v)):
    temp = math.fabs(v[i], v[i-1])
    if temp < diff:
        diff = temp

print(diff)
