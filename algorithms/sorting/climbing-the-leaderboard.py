input() # ignore input
scores = {}
for score in list(map(int, input().split())):
    if score in scores:
        scores[score] +=1
    else:
        scores[score] = 1

sorted_scores = sorted(scores.keys(), reverse=True)

input() # ignore input
place = len(sorted_scores) # start at the bottom of the leaderboard

for score in list(map(int, input().split())):
    # climb leaderboard
    while sorted_scores[place - 1] <= score and place > 0:
        place -= 1
    print(place + 1)
