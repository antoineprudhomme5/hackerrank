for _ in range(int(input())):
    c = 0
    d = {}
    for i in input():
        if i not in d:
            d[i] = 1
            c += 1
    print(c)