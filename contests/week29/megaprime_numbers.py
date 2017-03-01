import re
import math

# find all the primes numbers from 0 to end
def sieve_of_Eratosthenes(end):
    pass
    numbers = range(2, end)
    primes = []
    len_numbers = len(numbers)
    while len_numbers:
        next_numbers = []
        primes.append(numbers[0])
        for i in range(1, len_numbers):
            if numbers[i] % numbers[0] > 0:
                next_numbers.append(numbers[i])
        # prepare next loop
        numbers = next_numbers
        len_numbers = len(numbers)
    return primes


first, last = list(map(int, input().split()))
primes = sieve_of_Eratosthenes(last)
megaprimes = []

# save the primes which are megaprimes
for p in primes:
    if re.match(r'^([2357]+)$', str(p)):
        megaprimes.append(p)
print(len(megaprimes))
