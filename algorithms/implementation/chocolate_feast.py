for _ in range(int(input())):
    n, c, m = list(map(int, input().split()))

    wrappers = n // c
    total = wrappers

    # continue while it's possible to buy chocolates
    while wrappers >= m:
        # retrieve the chocolate coast and add the wrapper of the new chocolate
        wrappers += 1 - m
        total += 1

    print(total)
