for _ in range(int(input())):
    catA, catB, mouse = map(int, input().split())
    distA = abs(mouse - catA)
    distB = abs(mouse - catB)
    if distA == distB:
        print("Mouse C")
    else:
        print("Cat A" if distA < distB else "Cat B")
