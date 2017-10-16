nb_hurdles, max_height = map(int, input().split())
tallest_burdle = max(list(map(int, input().split())))
print(0 if tallest_burdle <= max_height else tallest_burdle - max_height)
