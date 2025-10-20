n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
grid=[[0]*m for _ in range(n)]
def inrange(x,y):
    return 0<=x<n and 0<=y<m
dr=[0,1,0,-1]
dc=[1,0,-1,0]
r=c=dir_num=0
grid[r][c]=1

for i in range(2,n*m+1):
    nr=r+dr[dir_num]
    nc=c+dc[dir_num]
    if not inrange(nr,nc) or grid[nr][nc]!=0:
        dir_num=(dir_num+1)%4
    r+=dr[dir_num]
    c+=dc[dir_num]
    grid[r][c]=i
for i in range(n):
    for j in range(m):
        print(grid[i][j],end=' ')
    print()
    