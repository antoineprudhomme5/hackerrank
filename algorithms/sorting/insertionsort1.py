n = int(input())
a = list(map(int, input().split()))

to_insert = a[n-1]
cursor = n - 1

while cursor > 0 and a[cursor - 1] > to_insert:
    a[cursor] = a[cursor - 1]
    print(' '.join(str(v) for v in a))
    cursor -= 1

a[cursor] = to_insert
print(' '.join(str(v) for v in a))