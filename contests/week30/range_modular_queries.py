def read_integers_list():
    return list(map(int, input().strip().split()))

def check_congruence(n, x, y):
    return int(n % x == y)

n, q = read_integers_list()
a = read_integers_list()

for _ in range(q):
    left, right, x, y = read_integers_list()
    count = 0
    for i in range(left, right+1):
        count += check_congruence(a[i], x, y)
    print(count)