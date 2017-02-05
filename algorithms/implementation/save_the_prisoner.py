for _ in range(int(input())):
    n, m, s = list(map(int, input().split()))
    # skip the complete turn
    r = (m + s - 1) % n
    print(n if r == 0 else r)