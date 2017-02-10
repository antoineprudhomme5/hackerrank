import string

def next_permutation(str):
    # Find non increasing suffix
    i = len(str) - 1
    while i > 0 and d[str[i-1]] >= d[str[i]]:
        i -= 1
    if i == 0:
        return 'no answer'

    pivot = i - 1

    # Find the lowest value grater than pivot in the suffix
    i = len(str) - 1
    while d[str[i]] <= d[str[pivot]]:
        i -= 1
    
    # do the permutation
    str[pivot], str[i] = str[i], str[pivot]

    # reverse suffix
    str[pivot + 1:] = str[len(str) - 1 : pivot : -1]

    return ''.join(str)

# create a dict with all alphabet letters and their values
d = {}
alphabet = string.ascii_lowercase
for c in range(len(alphabet)):
    d[alphabet[c]] = c

# for each test case
for _ in range(int(input())):
    print(next_permutation(list(input())))