import math

d = {}
for c in input():
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

values = list(d.values())
values.sort()

most_common = max(values, key=values.count)

to_remove = 0
for i in range(0, len(values)):
    if values[i] == 1:
        to_remove += 1
    else:
        to_remove += math.fabs(most_common - values[i])

print('NO' if to_remove > 1 else 'YES')
