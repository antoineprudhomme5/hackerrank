# for 0 <= X <= N
# count the X, where N+X = N^X
# => count number of 0 in the bin value of N and calcultate how many combinations we can make
# -1 to the 0 count because there is '0b' in front of the binary value
n = int(input().strip())
print(1 if n == 0 else 2 ** bin(n).lstrip('0').count('0'))
