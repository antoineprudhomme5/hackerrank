n, t = map(int, input().split())
chapters = sorted([int(input()) for _ in range(n)])
count = 0
for i in range(n):
    t -= chapters[i]
    if t < 0:
        break
    count += 1
print(count)
