def read_integers_list():
    return [int(v) for v in input().split()]

n, m = read_integers_list()
a = read_integers_list()
b = read_integers_list()

max_a = max(a)
min_b = min(b)

if max_a > min_b:
    print('0')
else:
    between = []
    for i in range(max_a, min_b+1):
        modulo_sum = 0
        for e in a:
            modulo_sum += i % e
        for e in b:
            modulo_sum += e % i
        if modulo_sum == 0:
            between.append(i)

    # +2 for max_a and min_b
    print(len(between))
