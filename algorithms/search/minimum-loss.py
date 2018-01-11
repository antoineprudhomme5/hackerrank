n = int(input())
p = list(map(int, input().split()))

# all prices are distinct
# remember the original pos of each price in the list
# because the order is important
dic = {}
for i, v in enumerate(p):
    dic[v] = i
# sort the prices => the diff between each pair is the min loss
p = sorted(p)

min_loss = float('+Inf')

# loop through each pair
for i in range(n-1):
    # check if the pair has a loss lower than the current min loss
    # and that the pair respects the original order
    if p[i+1] - p[i] < min_loss and dic[p[i+1]] < dic[p[i]]:
        min_loss = p[i+1] - p[i]

print(min_loss)
