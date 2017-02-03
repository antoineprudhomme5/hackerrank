n = int(input())
liked = 0
toShare = 5
while n > 0:
    toShare = toShare // 2
    liked += toShare
    toShare *= 3
    n -= 1
print(liked)