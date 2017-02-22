import math

def euclidian_dist(a_x, a_y, b_x, b_y):
    return math.sqrt(math.pow(a_x - b_x, 2) + math.pow(a_y - b_y, 2))

def is_in_circle(p_x, p_y, c_x, c_y, r):
    return math.sqrt(math.pow(p_x - c_x, 2) + math.pow(p_y - c_y, 2)) <= r

def triangle_area(a_x, a_y, b_x, b_y, c_x, c_y):
    a = euclidian_dist(a_x, a_y, b_x, b_y)
    b = euclidian_dist(b_x, b_y, c_x, c_y)
    c = euclidian_dist(c_x, c_y, a_x, a_y)
    p = (a + b + c) / 2
    temp = p * (p-a) * (p-b) * (p-c)
    #if (b_x == 13 and b_y == 12) or (b_x == 11 and b_y == 12):
        #print("%d => %d : %d %d %d" % (p, temp, a, b, c))
    if temp < 0:
        return 0
        # print("%d => %d : %d %d %d" % (p, temp, a, b, c))
    return math.sqrt(temp)

def is_in_square(p_x, p_y, a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
    areas_sum = triangle_area(a_x, a_y, p_x, p_y, b_x, b_y) + \
                triangle_area(b_x, b_y, p_x, p_y, c_x, c_y) + \
                triangle_area(c_x, c_y, p_x, p_y, d_x, d_y) + \
                triangle_area(d_x, d_y, p_x, p_y, a_x, a_y)
    #if (p_x == 13 and p_y == 12) or (p_x == 11 and p_y == 12):
        #print(areas_sum)
    # if the triangles areas sum is greater than the square area, it's outside
    return int(areas_sum) <= SQUARE_AREA

w, h = list(map(int, input().split()))
circleX, circleY, r = list(map(int, input().split()))
x1, y1, x3, y3 = list(map(int, input().split()))

half_diagonal = math.floor(euclidian_dist(x1, y1, x3, y3) / 2)

if x3 > x1:
    x2, y2 = x1 + half_diagonal, y3 - half_diagonal
    x4, y4 = x3 - half_diagonal, y1 + half_diagonal
else:
    x4, y4 = x3 + half_diagonal, y1 - half_diagonal
    x2, y2 = x1 - half_diagonal, y3 + half_diagonal

SQUARE_AREA = (x1-x2)**2 + (y1-y2)**2

for j in range(h):
    row = ['.'] * w
    for i in range(w):
        if is_in_circle(i, j, circleX, circleY, r) or is_in_square(i, j, x1, y1, x2, y2, x3, y3, x4, y4):
            row[i] = '#'
    print(''.join(row))
