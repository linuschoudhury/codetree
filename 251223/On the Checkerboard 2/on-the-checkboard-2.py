R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
startcolor=grid[0][0]
endcolor=grid[R-1][C-1]
validpaths=0
#for first jump
for row1 in range(1,R-2):
    for column1 in range(1,C-2):
        if grid[row1][column1]==startcolor:
            continue
        #for second jump
        for row2 in range(row1+1,R-1):
            for column2 in range(column1+1,C-1):
                if grid[row1][column1]==grid[row2][column2]:
                    continue
                if grid[row2][column2] != endcolor:
                    validpaths+=1
print(validpaths)


