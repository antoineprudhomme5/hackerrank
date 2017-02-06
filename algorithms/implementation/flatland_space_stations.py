n, m = list(map(int, input().split()))
stations = list(map(int, input().split()))
stations.sort()

## between the first city and the first stations
max_d = stations[0]

## between each stations
for i in range(m - 1):
    dist = (stations[i+1] - stations[i]) // 2
    if dist > max_d:
        max_d = dist

## between the last city and the last stations
dist = n-1 - stations[m-1]
if dist > max_d:
    max_d = dist

print(int(max_d))