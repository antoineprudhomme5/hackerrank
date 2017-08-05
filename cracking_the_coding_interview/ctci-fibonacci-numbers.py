f = {}

def fibonacci(n):
    if n <= 1:
        return n
    if n not in f:
        f[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return f[n]

n = int(input())
print(fibonacci(n))
