p, d, m, s = list(map(int, input().split()))

count = 0

current_price = p
while s >= current_price and current_price != m:
    count++
    s -= current_price
    current_price -= d
    if current_price < m:
        current_price = m

count += s // m

print(count)
