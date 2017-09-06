def count_region_size(grid, n, m, i, j):
    if i >= 0 and i < n and j >= 0 and j < m and grid[i][j]:
        grid[i][j] = 0
        count = 1
        count += count_region_size(grid, n, m, i-1, j-1)
        count += count_region_size(grid, n, m, i-1, j)
        count += count_region_size(grid, n, m, i-1, j+1)
        count += count_region_size(grid, n, m, i, j-1)
        count += count_region_size(grid, n, m, i, j+1)
        count += count_region_size(grid, n, m, i+1, j-1)
        count += count_region_size(grid, n, m, i+1, j)
        count += count_region_size(grid, n, m, i+1, j+1)
        return count
    return 0

def find_biggest_region(grid, n, m):
    biggest_region = 0
    # go through the grid
    for i in range(n):
        for j in range(m):
            # if filled and not already visited
            if grid[i][j]:
                temp = count_region_size(grid, n, m, i, j)
                if temp > biggest_region:
                    biggest_region = temp

    return biggest_region


n = int(input().strip())
m = int(input().strip())
grid = []
for _ in range(n):
     grid.append(list(map(int, input().strip().split(' '))))
print(find_biggest_region(grid, n, m))
