n = int(input())

def is_on_grid(p):
    return p['i'] >= 0 and p['i'] < n and p['j'] >= 0 and p['j'] < n

def knight(i, j):
    if i == j:
        return (n-1)//i if (n-1) % i == 0 else -1
    
    counter = 1
    previous = []
    currents = []

    # append the start to the current list
    currents.append({
        'j': n-1,
        'i': n-1
    })

    #print('===============')
    #print('j : %d -- i : %d' % (j, i))
    # try to reach (0, 0)
    # stop when current is empty (nothing to explore, and we are not at (0,0))
    # or when we reach (0, 0)
    while len(currents):
        #print('CURRENT')
        #print(currents)
        nexts = []
        # for each current positions
        for curr in currents:
            # calculate each new points we can reach
            new_points = [
                {
                    'i': curr['i'] + i,
                    'j': curr['j'] + j
                },
                {
                    'i': curr['i'] - i,
                    'j': curr['j'] + j
                },
                {
                    'i': curr['i'] + i,
                    'j': curr['j'] - j
                },
                {
                    'i': curr['i'] - i,
                    'j': curr['j'] - j
                },
                {
                    'i': curr['i'] + j,
                    'j': curr['j'] + i
                },
                {
                    'i': curr['i'] - j,
                    'j': curr['j'] + i
                },
                {
                    'i': curr['i'] + j,
                    'j': curr['j'] - i
                },
                {
                    'i': curr['i'] - j,
                    'j': curr['j'] - i
                }
            ]
            # for each new points
            for n_p in new_points:
                # continue only if on the grid
                if is_on_grid(n_p):
                    # if it's our goal return counter
                    if n_p['i'] == 0 and n_p['j'] == 0:
                        return counter
                    
                    # if this point is not in previous (not already visited), push it
                    if n_p not in previous and n_p not in nexts:
                        nexts.append(n_p)

            # put the current point on the previous
            previous.append(curr)           

        currents = nexts
        counter += 1
    
    # if it's impossible to reach (0,0)
    return -1


for i in range(1, n):
    row = []
    for j in range(1, n):
        row.append(str(knight(i, j)))
    print(' '.join(row))