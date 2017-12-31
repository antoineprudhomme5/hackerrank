n = int(input())

dic = {}

# read input list
max_x = float('-Inf')
for i in range(n):
    x, s = input().split()
    x = int(x)

    if i < (n//2):
        s = "-"

    if x in dic:
        dic[x].append(s)
    else:
        dic[x] = [s]

    max_x = max(max_x, x)

result = []

for i in range(max_x+1):
    if i in dic:
        result += dic[i] 

print(' '.join(result))
