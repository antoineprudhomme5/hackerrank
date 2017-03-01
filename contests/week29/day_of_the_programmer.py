d = '13'
m = '09'
y = int(input())
if y == 1918:
    # the 14 febuary is the 32th day of the 1918 year in Russia
    d = '26'
else:
    # julian calendar
    if y < 1918:
        # if it's a leap year, it's the 12 september
        if y % 4 == 0:
            d = '12'
    # gregorian calendar
    else:
        # if it's a leap year, it's the 12 september
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            d = '12'

print('%s.%s.%d' % (d, m, y))
