n = int(input())

def knight(i, j):
    if i == j:
        return (n-1)//i if (n-1) % i == 0 else -1

for i in range(1, n):
    row = []
    for j in range(1, n):
        row.append(knight(i, j))
    print(' '.join(row))