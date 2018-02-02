def solve(s):
    digits = [int(s[i]) for i in range(len(s))]
    ans = [0 for _ in range(len(s))]

    ans[0] = digits[0]
    for i in range(1, len(s)):
        ans[i] = ((i+1)*digits[i] + 10*ans[i-1]) % (10**9 + 7)

    return sum(ans)

print(solve(input()) % (10**9 + 7))
