def sam_rounding(n):
    if n > 37 and n % 5 > 2:
        n += 5 - n % 5
    return n

for _ in range(int(input())):
    print(sam_rounding(int(input())))
