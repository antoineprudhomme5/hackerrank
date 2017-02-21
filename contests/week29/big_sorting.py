n = int(input())
# read strings
a = []
for _ in range(n):
    a.append(int(input()))
# sort and print the result
a.sort()
for i in range(n):
    print(a[i])
