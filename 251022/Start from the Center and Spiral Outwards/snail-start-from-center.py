n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
dc = [-1, 0, 1, 0]
dr = [0, -1, 0, 1]
value=n*n
grid=[[0]*n for _ in range(n)]
dir_num=0
r=c=n-1
grid[r][c]=value
def inrange(x,y):
    return 0<=x<n and 0<=y<n and grid[x][y]==0
for i in range(1,n*n):
    nr=r+dr[dir_num]
    nc=c+dc[dir_num]
    if not inrange(nr,nc):
        dir_num=(dir_num+1)%4
    r=r+dr[dir_num]
    c=c+dc[dir_num]
    grid[r][c]=value-i
for i in range(n):
    for j in range(n):
        print(grid[i][j],end=' ')
    print()

