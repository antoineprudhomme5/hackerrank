n = int(input())
loaves = list(map(int, input().split()))

c = 0

for i in range(n):
    if i == n-1:
        if loaves[i] % 2 == 1:
            print("NO")
        else:
            print(c)
    else:
        if loaves[i] % 2 == 1:
            loaves[i] += 1
            loaves[i+1] += 1
            c += 2