# modified kaprekar 

p = int(input())
q = int(input())

kaprekar = []
for n in range(p, q+1):
    d = len(str(n))
    square = str(n**2)
    left = square[:len(square) - d]
    left = int(left) if left else 0
    right = int(square[len(square) - d:])
    if right > 0 and left + right == n:
        kaprekar.append(str(n))

if len(kaprekar):
    print(' '.join(kaprekar))
else:
    print('INVALID RANGE')