# 16 : 16 + 1 + 6
# 123 + 12 + 23 + 1 + 2 + 3
# 1234 + 123 + 234 + 12 + 23 + 34 + 1 + 2 + 3 + 4

# 1234
# 1
# 2 + 12
# 3 + 23 + 123 = 3 + 20 + 3 + 120 + 3 = 3*3 + 10(2 + 12)
# 4 + 34 + 234 + 1234 = 4 + 30 + 4 + 230 + 4 + 1230 + 4 = 4*4 + 10(3 + 23 + 123)

def solve(substring):
    s = [0]
    for i in range(len(substring)):
        s.append(int(substring[i])*(i+1) + 10*s[i])
    return sum(s)

print(solve(input()) % (10**9 + 7))
