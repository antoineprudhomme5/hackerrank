for _ in range(int(input())):
    b, w = list(map(int, input().split()))
    x, y, z = list(map(int, input().split()))

    # calculate the default prices
    w_g = y*w
    b_g = x*b

    # calculate the costs with convertions
    c_w = w * (x+z)
    c_b = b * (y+z)

    # compare and choose the lower values
    if c_w < w_g:
        w_g = c_w
    if c_b < b_g:
        b_g = c_b
    
    print(w_g + b_g)