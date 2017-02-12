n = int(input())
set = input().split()
subset = []

def is_prefix(p, set):
    p_len = len(p)
    for s in set:
        if len(s) > p_len:
            prefix = True
            for i in range(p_len):
                if p[i] != s[i]:
                    prefix = False
            if prefix:
                return True
    return False

# for each string of set
for s in set:
    # check if this string is a prefix
    if not is_prefix(s, set):
        # if not, add it to subset
        subset.append(s)

v = 0
# calc the subset
for s in subset:
    for c in s:
        v += ord(c)

print(v)