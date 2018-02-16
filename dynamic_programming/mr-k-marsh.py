import sys

m, n = map(int, input().split())

grid = []
for _ in range(m):
    grid.append(list(input()))

down = [[0 for _ in range(n)] for _ in range(m)]
for i in range(1, m):
    for j in range(n):
        down[i][j] = -1 if grid[i][j] == 'x' else (down[i-1][j]+1)

right = [[0 for _ in range(n)] for _ in range(m)]
for j in range(1, n):
    for i in range(m):
        down[i][j] = -1 if grid[i][j] == 'x' else down[i][j-1]+1

current_res = float('-Inf')

for i in range(1, m):
    for j in range(1, n):
        temp_res = down[i][j]*2 + right[i][j]*2
        current_res = max(current_res, temp_res)

print("impossible" if current_res <= 0 else current_res)
