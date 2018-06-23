def contains(s, pattern):
	i = 0
	for c in s:
		if c == pattern[i]:
			i += 1
		if i == len(pattern):
			return True
	return False

pattern = "hackerrank"
for _ in range(int(input())):
	s = input()
	print("YES" if contains(s, pattern) else "NO")