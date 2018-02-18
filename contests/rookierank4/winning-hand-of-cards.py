import itertools

n, m, x = map(int, input().split())
cards = list(map(int, input().split()))

def product_modulo(items, m):
    p = 1
    for item in items:
        p = (p*item)%m
    return p

counter = 0
for i in range(len(cards)):
    for hand in list(itertools.combinations(cards, i+1)):
        if product_modulo(hand, m) == x:
            counter += 1
print(counter)
