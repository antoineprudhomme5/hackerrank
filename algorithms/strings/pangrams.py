s = ''.join(i.lower() for i in input().split())
# create a dict from the string (10^3 len max)
d = {}
for c in s:
    if c not in d:
        d[c] = None
# check if the length of the dic is 26 (all the char inside)
print('pangram' if len(list(d)) == 26 else 'not pangram')