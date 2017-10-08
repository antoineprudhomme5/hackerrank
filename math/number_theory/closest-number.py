for _ in range(int(input())):
    a, b, x = map(int, input().split())
    # calculate a to the power of b
    n = a**b
    # start by saying that the result is the lower multiple
    res = n - (n%x)
    # if the diff is smaller with the greater multiple
    # res is the greater multiple
    if n % x > (x // 2):
        res += x
    print(int(res))
