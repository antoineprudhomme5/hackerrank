import math

# reverse an integer
def reverse_int(n):
    return int(str(n)[::-1])

def is_beautiful(x, k):
    if math.fabs(x - reverse_int(x)) % k == 0:
        return 1
    return 0

i, j, k = list(map(int, input().split()))
c = 0
for x in range(i, j+1):
    c += is_beautiful(x, k)
print(c)