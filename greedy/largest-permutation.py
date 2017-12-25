n, k = map(int, input().split())
a = list(map(int, input().split()))

m = {}
for i, v in enumerate(a):
    m[v] = i

# continue while not at the end of the list
# and still swaps to make
i = 0
while i < n and k > 0:
    # if it's not the max value we can put here
    if a[i] != n-i:
        # make a swap
        k -= 1
        # get the index of the value we want
        idx_to_swap = m[n-i]
        # set the new index of the current value
        m[a[i]] = idx_to_swap
        # swap
        a[i], a[idx_to_swap] = a[idx_to_swap], a[i]

    i += 1

print(' '.join([str(v) for v in a]))
