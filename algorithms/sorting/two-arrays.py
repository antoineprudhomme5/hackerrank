def solve(A, B, k):
    for i in range(n):
        if (A[i]+B[i]) < k:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A = sorted(A)
    B = sorted(B, reverse=True)

    print(solve(A, B, k))
