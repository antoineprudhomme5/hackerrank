def stones(n, a, b):
    if a == b:
        return (n-1) * a
    else:
        values = []
        if a > b:
            a, b = b, a
        for i in range(n-1, -1, -1):
            values.append(str(i*a + (n-1-i)*b))
        return ' '.join(values)

for _ in range(int(input())):
    n = int(input())
    a = int(input())
    b = int(input())
    print(stones(n, a, b))