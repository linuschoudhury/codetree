n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dx=[0,1,0,-1]
dy=[1,0,-1,0]
cnt=0

for i in range(n):
    for j in range(n):
        count=0
        for dir_num in range(4):
            nx,ny=i+dx[dir_num],j+dy[dir_num]
            if 0<=nx<n and 0<=ny<n and grid[nx][ny] == 1:
                count+=1
        if count>=3:
            cnt+=1            
print(cnt)
