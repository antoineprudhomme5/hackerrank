def check_pattern(g, p, p_r, p_c, r, c):
    for j in range(p_r):
        for i in range(p_c):
            if g[r+j][c+i] != p[j][i]:
                return False
    return True

# for each test case
for _ in range(int(input())):
    # read the grid
    g_r, g_c = [int(v) for v in input().split()]
    g = []
    for _ in range(g_r):
        g.append(list(input()))
    # read the pattern
    p_r, p_c = [int(v) for v in input().split()]
    p = []
    for _ in range(p_r):
        p.append(list(input()))
    
    # loop throught the grid
    r = 0
    flag = False
    while r <= (g_r - p_r) and flag == False:
        c = 0
        while c <= (g_c - p_c) and flag == False:
            # if the cell has the same value as the first cell of the pattern
            if g[r][c] == p[0][0]:
                flag = check_pattern(g, p, p_r, p_c, r, c)
            c +=1
        r +=1
    
    # display answer
    print("YES" if flag else "NO")