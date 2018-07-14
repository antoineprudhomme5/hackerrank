n = int(input())
a = list(map(int, input().split()))

def solve(n, a):
    for i in range(n):
        if a[a[i]-1] != (i+1): 
            return False
    return True

print("YES" if solve(n, a) else "NO")