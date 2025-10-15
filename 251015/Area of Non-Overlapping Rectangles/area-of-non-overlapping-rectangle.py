x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
offset=1000
max_r=2000
n=3
rects=[]
count=0
for i in range(n):
    rects.append([x1[i]+offset,y1[i]+offset,x2[i]+offset,y2[i]+offset])


checked=[
    [0]*(2001) for _ in range(2001)
]
for i in range(3):
    for x in range(rects[i][0],rects[i][2]):
        for y in range(rects[i][1],rects[i][3]):
            checked[x][y]=i+1
            
for a in range(len(checked)):
    for b in range(len(checked[i])):
        if checked[a][b]==1 or checked[a][b]==2:
            count+=1
print(count)