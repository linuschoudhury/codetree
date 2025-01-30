n,m=map(int,input().split())
grid=[[0]*n for i in range(n)]
count=0
for i in range(m):
    r,c=tuple(map(int,input().split()))
    count+=1
    grid[r-1][c-1]=count
for i in range(n):
    for j in range(n):
        print(grid[i][j],end=' ')
    print()