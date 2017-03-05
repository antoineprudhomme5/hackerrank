n = int(input())
heights = list(map(int, input().split()))
areas = []
# go throught each building
for b in range(n):
    neighbors = 0
    # count taller neighbors
    for i in range(b, -1, -1):
        if heights[i] < heights[b]:
            break
        neighbors += 1
    for i in range(b+1, n):
        if heights[i] < heights[b]:
            break
        neighbors += 1
    # calculate the max area, with the current building as the smaller
    areas.append((neighbors) * heights[b])
print(max(areas))