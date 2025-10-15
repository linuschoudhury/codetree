n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
x2=[0]*n
y2=[0]*n
for i in range(n):
    x2[i]=x[i]+8
    y2[i]=y[i]+8
ymax = max(y)+max(y2)
xmax = max(x)+max(x2)
checked=[[0]*108 for _ in range(108)]
for i in range(n):
    for j in range(x[i],x2[i]):
        for k in range(y[i],y2[i]):
            checked[j][k]=1
            #print(j,k)
print(sum(sum(row) for row in checked))
