def reverse_binary(b):
    b = list(b)
    for i in range(len(b)):
        # because 32b format put spaces, not 0
        b[i] = '1' if b[i] == '0' or b[i] == ' ' else '0'
    return ''.join(b)

for _ in range(int(input())):
    # int to 32b value
    b = '{0:32b}'.format(int(input()))
    print(int(reverse_binary(b), 2))
