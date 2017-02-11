# if n = 12 and k = 3, for example
# 4 5 6 1 2 3 10 11 12 7 8 9
# for the next k*2 numbers, put first the second k part

# for each test case
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if k == 0 or n % k == 0:
        numbers = list(range(1, n+1))
        if k != 0:
            # for each chunk
            for c in range(n // (2*k)):
                chunk_i = c * (2*k)
                # reverse each part of the chunk
                for i in range(k):
                    numbers[chunk_i + i], numbers[chunk_i + i + k] = numbers[chunk_i + i + k], numbers[chunk_i + i]
                    
        print(' '.join([str(i) for i in numbers]))
    else:
        print('-1')
