n, scores = int(input()), list(map(int, input().split()))
highest, lowest = scores[0], scores[0]
highest_c, lowest_c = 0, 0
for i in range(1, n):
    if scores[i] < lowest:
        lowest = scores[i]
        lowest_c += 1
    elif scores[i] > highest:
        highest = scores[i]
        highest_c += 1
print("%d %d" % (highest_c, lowest_c))
