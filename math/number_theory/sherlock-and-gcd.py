def gcd(a, b):
	# 'a' has to be greater than 'b'
	if b > a:
		a, b = b, a
	# calculate the remainder of a/b
	remainder = a % b
	# if remainder is 0, stop here : gcd found
	if remainder == 0:
		return b
	return gcd(b, remainder)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    whole_gcd = a[0]
    for i in range(1, n):
        whole_gcd = gcd(whole_gcd, a[i])

    print("YES" if whole_gcd == 1 else "NO")
