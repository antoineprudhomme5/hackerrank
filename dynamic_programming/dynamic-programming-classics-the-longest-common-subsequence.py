import sys

def longest_common_subsequence(a, b, n, m):
    # init table
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    # fill table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if b[i-1] == a[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # trace back the longest common subsequence
    length = dp[m][n]
    common_subsquence = []
    curr_row, curr_col = m, n
    while length:
        if a[curr_col-1] == b[curr_row-1]:
            common_subsquence.append(b[curr_row-1])
            curr_row -= 1
            curr_col -= 1
            length -= 1
        else:
            # go to max value
            if dp[curr_row-1][curr_col] > dp[curr_row][curr_col-1]:
                curr_row -= 1
            else:
                curr_col -= 1

    return common_subsquence[::-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(input().split())
    b = list(input().split())
    print(' '.join(longest_common_subsequence(a, b, n, m)))
