n, k = list(map(int, input().split()))
c = list(map(int, input().split()))
b_charged = int(input())
b_actual = sum(c) // 2 - c[k] // 2
print('Bon Appetit' if b_charged == b_actual else c[k] // 2)