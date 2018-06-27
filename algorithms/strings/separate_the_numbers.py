def solve(s):
	curr_length = 1
	# try all possible numbers of digits for the first number
	while curr_length <= (len(s) // 2):
		# check if it works
		curr = s[0:curr_length]
		i = curr_length
		while i < len(s):
			next = str(int(curr) + 1)
			if s[i:i+len(next)] != next:
				# it's not working, leave the current loop
				break
			# it's fine for the moment, keep going
			curr = next
			i += len(next)
		# it works, return the first of the sequence
		if i == len(s):
			return s[0:curr_length]
		# increase the size and keep searching
		curr_length += 1
	return 0

# for each query
for _ in range(int(input())):
	v = solve(input())
	print(("YES " + v) if v else "NO")
