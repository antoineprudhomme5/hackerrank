input() # ignore the first input
print(sum(c*(2**j) for (j, c) in enumerate(sorted(list(map(int, input().split())), reverse=True))))
