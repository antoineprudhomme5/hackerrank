# triplet A < B < C
# where B = A*r and C = A*r*r = B*r


def count_triplets(arr, r):
    dict_A = {}
    dict_B = {}
    triplets_count = 0

    for v in arr:
        p = v / r

        # check if `v` is a C
        if p in dict_B:
            triplets_count = triplets_count + dict_B.get(p)

        # check if `v` is a B
        if p in dict_A:
            if v in dict_B:
                dict_B[v] = dict_B[v] + dict_A[p]
            else:
                dict_B[v] = dict_A[p]

        # `v` can be a A
        if v in dict_A:
            dict_A[v] = dict_A[v] + 1
        else:
            dict_A[v] = 1

    return triplets_count
