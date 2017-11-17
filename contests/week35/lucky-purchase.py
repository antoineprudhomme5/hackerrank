def match_criteria(s):
    d = {'7': 0, '4': 0}
    for c in s:
        if c is '7' or c is '4':
            d[c] += 1
        else:
            return False

    return d['7'] == d['4']


matches = []
for _ in range(int(input())):
    name, price = input().split()
    if match_criteria(price):
        matches.append((int(price), name))
matches.sort()
print(matches[0][1] if len(matches) else -1)
