# for each test case
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print('Richard')
    else:
        counter = 0
        while n != 1:
            if (n & n-1) == 0:
                n //= 2
            else:
                bin_n = bin(n)[2:]
                msb_i = bin_n.find('1')
                n -= 2**(len(bin_n) - 1 - msb_i)
            counter += 1
        if counter % 2 == 0:
            print('Richard')
        else:
            print('Louise')
