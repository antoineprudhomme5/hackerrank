s = input()
n = int(input())

# number of times we can count on the full string
f = n // len(s)
# number of char to check on the remaining string part
r = n % len(s)

counter = s.count('a') * f + s[:r].count('a')

print(counter)