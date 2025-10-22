R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
currx=curry=0
count=0
for i in range(currx+1,R-1):
    for j in range(curry+1,C-1):
        if grid[i][j]!=grid[currx][curry]:
            count+=1
            currx=i
            curry=j
print(count)
        
