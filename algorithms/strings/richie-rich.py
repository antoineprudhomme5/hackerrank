n, k = map(int, input().split())
c = list(map(int, list(input())))

# fist, count how many changes to do for c to be a palindrome
for i in range(n // 2):
    if c[i] != c[n-i-1]:
        k -= 1

# if k too low, c can't be a palindrome
if k < 0:
    print(-1)
else:
    for i in range(n // 2):
        # if differents, make the change
        if c[i] != c[n-i-1]:
            v = max(c[i], c[n-i-1])
            # if we can make more changes, make the number bigger
            if v != 9 and k > 0:
                k -= 1
                v = 9
            c[i] = c[n-i-1] = v
        # if not differents but we can make 2 changes,
        # set both to 9 to make the number bigger
        elif c[i] != 9 and k >= 2:
            c[i] = c[n-i-1] = 9
            k -= 2

    # if the number has an odd length and a change is still availabe,
    # set the digit at the middle to 9
    if n % 2 == 1 and k:
        c[n//2] = 9

    print(''.join(list(map(str, c))))
