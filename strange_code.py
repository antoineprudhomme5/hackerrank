t = int(input())
cycle = 0
start = 1
end = 3
while t > end:
    cycle += 1
    start = end+1
    end = end*2 + 3
print(end - t + 1)