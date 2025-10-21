n, m = map(int, input().split())

# Please write your code here.
grid=[[0]*m for _ in range (n)]
r=c=0
dr=[1,0,-1,0]
dc=[0,1,0,-1]
dir_num=0
def inrange(x,y):
    return 0<=x<n and 0<=y<m and grid[x][y]==0
grid[0][0]=1
for i in range(2,m*n+1):
    nr=r+dr[dir_num]
    nc=c+dc[dir_num]
    if not inrange(nr,nc):
        dir_num=(dir_num+1)%4
    r=r+dr[dir_num]
    c=c+dc[dir_num]
    grid[r][c]=i
for i in range(n):
    for j in range(m):
        print(grid[i][j],end=' ')
    print()
