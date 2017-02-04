import string
alphabet = string.ascii_lowercase
heights = list(map(int, input().split()))
s = input()
tallest = 1
for i in s:
    temp = heights[alphabet.index(i)]
    if temp > tallest:
        tallest = temp
print(tallest * len(s))