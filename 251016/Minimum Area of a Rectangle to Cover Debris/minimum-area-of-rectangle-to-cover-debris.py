x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Check if there's any intersection
intersect_x1 = max(x1[0], x1[1])
intersect_y1 = max(y1[0], y1[1])
intersect_x2 = min(x2[0], x2[1])
intersect_y2 = min(y2[0], y2[1])

if intersect_x1 >= intersect_x2 or intersect_y1 >= intersect_y2:
    print((x2[0] - x1[0]) * (y2[0] - y1[0]))
else:
    # There is intersection - check if rectangle 2 completely covers rectangle 1
    if x1[1] <= x1[0] and x2[1] >= x2[0] and y1[1] <= y1[0] and y2[1] >= y2[0]:
        print(0)
    else:
        print((x2[0] - x1[0]) * (y2[0] - y1[0]))



    




    

