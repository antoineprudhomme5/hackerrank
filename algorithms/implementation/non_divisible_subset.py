def to_next_multiple_of_k(n, k):
    comp = 0
    while (n + comp) % k != 0:
        comp += 1
    return comp

n, k = [int(v) for v in input().split()]
d = {}
for i in input().split():
    i = int(i)
    if i in d:
        d[i] += 1
    else:
        # find the complement to the next multiple of k
        comp = to_next_multiple_of_k(i, k)
        # find in the dict if there is no number which can make a multiple of 3
        if comp not in d:
            valid = True
            for key, value in d.items():
                if (key - comp) % k == 0:
                    valid = False
                    break
            # if the number is ok, put it in the dict
            d[i] = 1

print(len(d.items()))
