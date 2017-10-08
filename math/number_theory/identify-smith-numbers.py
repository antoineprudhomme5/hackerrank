def sum_digits(n):
    n = str(n)
    return sum([int(d) for d in n])

def prime_factorization(n, primes = []):
    if n <= 1:
        return primes

    i = 2
    while not n % i == 0:
            i +=1
    primes.append(i)

    return prime_factorization(n // i, primes)

n = input()
print(1 if sum_digits(n) == sum([sum_digits(v) for v in prime_factorization(int(n))]) else 0)
