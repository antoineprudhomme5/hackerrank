for _ in range(int(input())):
    str_n = input()
    n = int(str_n)
    str_n = [int(v) for v in str_n]

    count = 0
    for d in str_n:
        if d > 0 and n % d == 0:
            count += 1
    print(count)