# for each test case
for _ in range(int(input())):
    n = int(input())
    # because (1^2)^(2^3) = 1^2^2^3 = 1^3
    # just take the numbers which appears an odd number of time, and make xor between them
    # to find the number which appears an odd number of time, there is a pattern :
    #   - if array length is even => it's 0 because numbers all appears an even number of time
    #   - else, pick the elements at index 0, 2, 4, ... (they appears an odd number of time)
    a = list(map(int, input().split()))
    len_a = len(a)
    if len_a % 2 == 0:
        print(0)
    else:
        res = a[0]
        for i in range(2, len_a, 2):
            res ^= a[i]
        print(res)
