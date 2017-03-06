def read_integers():
    return list(map(int, input().split()))

""" is the heights of the stacks equals ?
"""
def are_equals(heights):
    for i in range(1, len(heights)):
        if heights[i-1] != heights[i]:
            return False
    return True

# read the number of cylinders of each stack
nb_cylinders = read_integers()
# read the cylinders heights
stacks = [read_integers()[::-1] for i in range(3)]
# calculate the height of each stack
stacks_heights = [sum(stack) for stack in stacks]
# while the heights are not the same
while not are_equals(stacks_heights):
    # remove the top cylinder of the highest stack
    highest = stacks_heights.index(max(stacks_heights))
    stacks_heights[highest] -= stacks[highest].pop()
# now, they all have the same height : print this height
print(stacks_heights[0])
