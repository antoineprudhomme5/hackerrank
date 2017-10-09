n = int(input()) + 1
values = [0] * n

x = 1
for px in map(int, input().split()):
    values[px] = x
    x += 1

for i in range(1, n):
    print(values[values[i]])
