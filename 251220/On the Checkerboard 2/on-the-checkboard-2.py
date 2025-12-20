R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
cnt=0
for i in range(R-2):
    for j in range(C-2):
        for k in range(i+1,R-1):
            for l in range(j+1,C-1):
                if grid[i][j]!=grid[k][l]:
                    cnt+=1
print(cnt-2)
                