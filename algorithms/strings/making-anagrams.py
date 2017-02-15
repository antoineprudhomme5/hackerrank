import math
a, b = input(), input()
counter = 0
for i in set(a) | set(b):
    counter += math.fabs(a.count(i) - b.count(i))
print(int(counter))
