n = int(input())
m = int(input())

grid = []
for _ in range(n):
	grid.append(input().split())

def rec(row, col):
	# if out of the grid
	if row < 0 or row >= n or col < 0 or col >= m:
		return 0
	# if cell not filled
	if grid[row][col] == "0":
		return 0
	# cell filled !
	# set to 0 (~= visited)
	# and add 1 and recursive call
	grid[row][col] = "0"
	return 1 + rec(row-1, col-1) + rec(row-1, col) + rec(row-1, col+1) \
		+ rec(row, col-1) + rec(row, col+1) + rec(row+1, col-1) + rec(row+1, col) \
		+ rec(row+1, col+1)

current_max = 0

for row in range(n):
	for col in range(m):
		if grid[row][col] == "1":
			current_max = max(current_max, rec(row, col))

print(current_max)