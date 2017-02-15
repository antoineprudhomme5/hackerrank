# for each pair to check
for _ in range(int(input())):
    a = set(input())
    b = set(input())
    print('YES' if (a & b) else 'NO')
