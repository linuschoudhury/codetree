n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

maxcount=0
for i in range(n):
    count=0
    for j in range(n-2):
        maxcount=max(maxcount,grid[i][j]+grid[i][j+1]+grid[i][j+2])
print(maxcount)
        

