initial = input()
final = input()
k = int(input())

# calculate the common length of the 2 strings
common_length = 0
for i in range(min(len(initial), len(final))):
    if initial[i] != final[i]:
        break
    common_length += 1

# remove the next characters in the initial string and append
# the characters of the final string
diff = len(initial) + len(final) - common_length*2

# we have to do exactly k operations (we can add + remove char -> that's why %) 
print("Yes" if (diff <= k and diff%2 == k%2) or len(initial) + len(final) < k else "No")
