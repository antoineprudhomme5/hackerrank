n = int(input())
# read strings
a = [0] * n
for i in range(n):
    a[i] = int(input())
# sort and print the result
a.sort()
for i in range(n):
    print(a[i])
