def read_in_dict():
    dic = {}
    for i in input().split():
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

n = int(input())
A = read_in_dict()
m = int(input())
B = read_in_dict()

missings = []
for k, v in B.items():
    if (k not in A) or (v != A[k]):
        missings.append(k)
missings.sort()
print(' '.join(missings))
