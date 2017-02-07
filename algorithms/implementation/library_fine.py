r_d, r_m, r_y = list(map(int, input().split()))
e_d, e_m, e_y = list(map(int, input().split()))

fine = 0

# if returned after the expected year
if e_y < r_y:
    fine = 10000
elif e_y == r_y:
    # if returned after the expected month
    if e_m < r_m:
        fine = 500 * (r_m - e_m)    
    elif e_m == r_m:
        # if returned after the expected day
        if e_d < r_d:
            fine = 15 * (r_d - e_d)

print(fine)