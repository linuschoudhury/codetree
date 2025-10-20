n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
dx=[0,0,-1,1]
dy=[1,-1,0,0]
grid=[[0]*n for _ in range(n)]
def inrange(x,y):
    return 0<=x<n and 0<=y<n

for i in range(m):
    comfortable=0
    count=0
    grid[points[i][0]-1][points[i][1]-1]=1
    x=points[i][0]-1
    y=points[i][1]-1
    for j in range(4):
        nx=x+dx[j]
        ny=y+dy[j]
        if inrange(nx,ny) and grid[nx][ny]==1:
            count+=1
    if count==3:
        comfortable=1
    print(comfortable)



    
