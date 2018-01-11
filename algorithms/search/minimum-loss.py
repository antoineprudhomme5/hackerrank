n = int(input())
p = list(map(int, input().split()))

min_loss = float('+Inf')

for i in range(n-2, -1, -1):
    # search the biggest value lower or equal than the current value
    for j in range(i+1, n):
        if p[i] >= p[j]:
            min_loss = min(min_loss, p[i]-p[j])
            break
    # keep the tail of the list sorted
    current = i
    while current < n-1 and p[current] < p[current+1]:
        p[current], p[current+1] = p[current+1], p[current]
        current += 1

print(min_loss)
