def is_on_house(p, s, t):
    if p >= s and p <= t:
        return 1
    return 0

s, t = list(map(int, input().split())) # house start and end positions
a, b = list(map(int, input().split())) # apple tree and orange tree coordinates
m, n = list(map(int, input().split())) # number of apples and oranges

c_a = 0
c_o = 0

apples = list(map(int, input().split()))
for d in apples:
    p = a + d
    c_a += is_on_house(p, s, t)

oranges = list(map(int, input().split()))
for d in oranges:
    p = b + d
    c_o += is_on_house(p, s, t)

print(c_a)
print(c_o)