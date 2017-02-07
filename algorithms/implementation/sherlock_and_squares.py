import math

def next_square(i):
    return math.pow(i+1, 2)

for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    i = math.ceil(math.sqrt(a) -1)
    count = 0
    square = next_square(i)

    # if the square is in the range, increment the counter and calc the next square
    while square <= b:
        count += 1
        i += 1
        square = next_square(i)

    print(count)