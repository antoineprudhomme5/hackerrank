s = input()
t = input()
k = int(input())
root_len = 0
c = 0
# get common part
for i in range(len(t)):
    if i < len(s) and s[i] == t[i]:
        root_len += i
    else:
        break
# count the number of letters to remove from s
c += len(s) - root_len
# count the number of letters to add to s
c += len(t) - root_len

# if remaining is even, it's ok
# or if we can delete on empty string many time before built it again
r = (c <= k) and (((k - c) % 2 == 0) or ((k / len(t)) >= 2))

print('Yes' if r else 'No')