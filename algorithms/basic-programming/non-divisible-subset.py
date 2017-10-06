""" Work with remainders. If the A/K + B/K != K, it's ok
"""
n, k = map(int, input().split())

remainders = {}
# init the counter of each possible remainder to 0
for i in range(0, k):
    remainders[i] = 0
# count the remainders
for n in input().split():
    remainders[int(n) % k] += 1

m = min(remainders[0], 1)
# k//2+1 because we check both i and k-i on each loop
for i in range(1, k//2+1):
    if i != k-i:
        m += remainders[i] if remainders[i] > remainders[k-i] else remainders[k-i]
if k % 2 == 0:
    m += 1
print(m)
