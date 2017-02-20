# for each test case
for _ in range(int(input())):
    m = int(input())
    n = int(input())
    c = list(map(int, input().split()))
    # store the complements in a dic
    complements = {}
    for i in range(n):
        complement = m - c[i]
        # if the complement exist, we found the solution
        if complement in complements:
            print("%d %d" % (complements[complement] + 1, i + 1))
            break
        # else, store the complement of this flavor, and continue
        else:
            complements[c[i]] = i
