x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
offset=1000
checked = [[0] * 2001 for _ in range(2001)]
A=set()
x1_0, y1_0, x2_0, y2_0=x1[0]+offset, y1[0]+offset, x2[0]+offset, y2[0]+offset
x1_1, y1_1, x2_1, y2_1=x1[1]+offset, y1[1]+offset, x2[1]+offset, y2[1]+offset
del x1,x2,y1,y2
for i in range(min(x1_0,x2_0),max(x1_0,x2_0)):
    for j in range(min(y1_0,y2_0),max(y1_0,y2_0)):
        checked[i][j]=1

for i in range(min(x1_1,x2_1),max(x1_1,x2_1)):
    for j in range(min(y1_1,y2_1),max(y1_1,y2_1)):
        checked[i][j]=2
min_x,min_y=2001,2001
max_x,max_y=0,0
overlapped=False
for i in range(len(checked)):
    for j in range(len(checked[i])):
        if checked[i][j]==1:
            overlapped=True
            min_x=min(i,min_x)
            max_x=max(i,max_x)
            min_y=min(j,min_y)
            max_y=max(j,max_y)
if overlapped==True: 
    print(((max_x-min_x)+1)*((max_y-min_y)+1))
else:
    print(0)





    




    


