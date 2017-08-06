m = {}

def calc_number_of_ways(n):
    if n not in m:
        if n >= 3:
            m[n] = calc_number_of_ways(n-3) + calc_number_of_ways(n-2) + calc_number_of_ways(n-1)
        elif n == 2:
            m[n] = 2
        else:
            m[n] = 1

    return m [n]

for _ in range(int(input())):
    print(calc_number_of_ways(int(input())))
