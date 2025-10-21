n, m = map(int, input().split())

# Please write your code here.
A=65
grid=[[0]*m for _ in range(n)]
dr=[0,1,0,-1]
dc=[1,0,-1,0]
r=c=0
grid[r][c]='A'
dir_num=0
count=0
def inrange(x,y):
    return 0<=x<n and 0<=y<m and grid[x][y]==0
for i in range(n*m-1):
    nr=r+dr[dir_num]
    nc=c+dc[dir_num]
    if not inrange(nr,nc):
        dir_num=(dir_num+1)%4
    r=r+dr[dir_num]
    c=c+dc[dir_num]
    count+=1
    if count==26:
        count=0
    grid[r][c]=chr(A+count)
for i in range(n):
    for j in range(m):
        print(grid[i][j],end=' ')
    print()
