s, n, m = map(int, input().split())

keyboard_remainings = []
for price in list(map(int, input().split())):
    remaining = s - price
    if remaining > 0:
        keyboard_remainings.append(remaining)
keyboard_remainings.sort(reverse=True)

# init with default value (can't buy)
max_spending = -1

for price in list(map(int, input().split())):
    # compare to keyboard_remainings
    for remaining in keyboard_remainings:
        if remaining < price:
            # list is sorted so stop here
            break
        if remaining == price:
            # found the max spending, stop here
            max_spending = s
            break

        # check if the coast his higher than the current
        temp_spending = s - (remaining - price)
        if temp_spending > max_spending:
            # if it's the case, update max_spending
            max_spending = temp_spending

print(max_spending)
