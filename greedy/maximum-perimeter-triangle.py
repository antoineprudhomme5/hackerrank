n = int(input())
sticks = list(map(int, input().split()))

def solve(sticks, current):
    if current >= (len(sticks)-2):
        return -1

    if sticks[current] < (sticks[current+1] + sticks[current+2]):
        return '%d %d %d' % (sticks[current+2], sticks[current+1], sticks[current])

    return solve(sticks, current+1)

sticks = sorted(sticks, reverse=True)
print(solve(sticks, 0))
