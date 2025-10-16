x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
offset=1000
A=set()
x1[0], y1[0], x2[0], y2[0]=x1[0]+offset, y1[0]+offset, x2[0]+offset, y2[0]+offset
x1[1], y1[1], x2[1], y2[1]=x1[1]+offset, y1[1]+offset, x2[1]+offset, y2[1]+offset
for i in range(min(x1[0],x2[0]),max(x1[0],x2[0])):
    for j in range(min(y1[0],y2[0]),max(y1[0],y2[0])):
        A.add((i,j))

for i in range(min(x1[1],x2[1]),max(x1[1],x2[1])):
    for j in range(min(y1[1],y2[1]),max(y1[1],y2[1])):
        A.discard((i,j))
if A:
    #x_coords = max([point[0] for point in A])
    #y_coords = max([point[1] for point in A])
    x_max = max([point[0] for point in A]) + 1
    x_min = min([point[0] for point in A])

    y_max = max([point[1] for point in A])+1
    y_min = min([point[1] for point in A])
    print((x_max-x_min)*(y_max-y_min))
else:
    print(0)




    




    


