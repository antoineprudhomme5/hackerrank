n = int(input())
d = {}

# for each birds, increment the type counter in the dic
for b in input().split():
    if b in d:
        d[b] += 1
    else:
        d[b] = 1

# find and print the most common
most_common = '1'
for t, c in d.items():
    if c > d[most_common] or (c == d[most_common] and int(t) < int(most_common)):
        most_common = t
print(most_common)
