n = int(input())
numbers = list(map(int, input().split()))
d, m = map(int, input().split())

counter = 0

# handle special case
if m == 1 and n == 1 and numbers[0] == d:
    counter += 1
# if m greater than n, it's impossible
# => not enough squares in the bar
elif m <= n:
    # init
    low = 0
    high = m - 1
    window_sum = sum(numbers[0:m])

    # loop til the end
    while True:
        # if window_sum is d, increment counter
        if window_sum == d:
            counter += 1

        # slide the window if possible
        if high == n - 1:
            break

        # don't need to recalculate all :
        # juste remove the first and add the next
        window_sum -= numbers[low]
        low += 1
        high += 1
        window_sum += numbers[high]

print(counter)
