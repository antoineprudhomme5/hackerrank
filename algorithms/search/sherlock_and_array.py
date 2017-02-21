for _ in range(int(input())):
    n = int(input())
    a = [int(v) for v in input().split()]
    if n == 1:
        print("YES")
    else:
        # create an array with all the left sum of each index
        left_sums = [0] * n
        left_sums[0] = a[0]
        for i in range(1, n):
            left_sums[i] = a[i] + left_sums[i-1]
        # find if it exists left_sums[i] where the previous is equal to (the last - the current)
        found = False
        for i in range(1, n):
            if left_sums[i-1] == (left_sums[n-1] - left_sums[i]):
                found = True
                break
        print("YES" if found else "NO")
