def solve(year):
    if year == 1918:
        return '26.09.1918'
    else:
        leap = year % 4 == 0
        if year > 1918:
            leap = (leap and year % 100 != 0) or (year % 400 == 0)
        return '12.09.%s' %year if leap else '13.09.%s' %year

print(solve(int(input())))
