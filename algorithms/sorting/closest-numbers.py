n = int(input())
arr = sorted(list(map(int, input().split())))

r = [0]

for i in range(1, n-1):
    d = abs(arr[r[0]+1]-arr[r[0]])
    new_d = abs(arr[i+1]-arr[i])
    if d > new_d:
        r = [i]
    elif d == new_d:
        r.append(i)

print(" ".join(["%d %d" % (arr[i], arr[i+1]) for i in r]))
