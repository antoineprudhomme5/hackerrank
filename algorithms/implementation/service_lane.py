n, t = list(map(int, input().split()))
segments = list(map(int, input().split()))
for _ in range(t):
    i, j = list(map(int, input().split()))
    print(min(segments[i:j+1]))