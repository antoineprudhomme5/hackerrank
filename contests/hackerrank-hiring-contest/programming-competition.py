n = int(input())
winner_name = None
winner_count = float('-Inf')
for _ in range(n):
    name, d, j = input().split()
    d, j = int(d), int(j)
    diff = j - d
    if diff > winner_count:
        winner_name = name
        winner_count = diff
print(winner_name + " " + str(winner_count))
