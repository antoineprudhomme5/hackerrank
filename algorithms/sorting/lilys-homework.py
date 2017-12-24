n = int(input())
a = list(map(int, input().split()))

def solve(a, n, sorted_a):
    m = {}
    for i in range(n):
        m[a[i]] = i

    nb_swaps = 0

    for i in range(n):
        if a[i] != sorted_a[i]:
            nb_swaps += 1

            idx_to_swapp = m[sorted_a[i]]
            m[a[i]] = idx_to_swapp
            # swapp
            a[i], a[idx_to_swapp] = a[idx_to_swapp], a[i]

    return nb_swaps

cpy_a = list(a)
s1 = solve(a, n, sorted(a))
s2 = solve(cpy_a, n, sorted(cpy_a)[::-1])

print(min(s1, s2))
