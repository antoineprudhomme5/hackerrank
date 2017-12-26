def cols_sorted(grid, n):
    for j in range(n):
        for i in range(1, n):
            if grid[i-1][j] > grid[i][j]:
                return False

    return True


for _ in range(int(input())):
    n = int(input())
    grid = [sorted(list(input())) for _ in range(n)]

    print("YES" if cols_sorted(grid, n) else "NO")
