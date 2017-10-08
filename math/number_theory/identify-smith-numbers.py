def sum_digits(n):
    n = str(n)
    return sum([int(d) for d in n])

def prime_factorization(n, primes = []):
    if n <= 1:
        return primes

    i = 2
    flag = False
    while not flag:
        if n % i == 0:
            flag = True
            primes.append(i)
        else:
            i +=1

    return prime_factorization(n // i, primes)

n = input()
print(1 if sum_digits(n) == sum([sum_digits(v) for v in prime_factorization(int(n))]) else 0)
