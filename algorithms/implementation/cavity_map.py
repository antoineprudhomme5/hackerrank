def is_cavity(m, y, x):
    v = m[y][x]
    return (v > m[y+1][x]) and (v > m[y-1][x]) and (v > m[y][x+1]) and (v > m[y][x-1])

m = []
n = int(input())
for _ in range(n):
    m.append(input())

for y in range(1, n-1):
    for x in range(1, n-1):
        if is_cavity(m, y, x):
            t = list(m[y])
            t[x] = 'X'
            m[y] = ''.join(t)

for i in range(n):
    print(''.join(m[i]))