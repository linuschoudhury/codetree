N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
dc = [1, 0, -1, 0, 1, -1, 1, -1]
dr = [0, 1, 0, -1, 1, 1, -1, -1]
count=0
def inrange(x,y):
    return 0<=x<N and 0<=y<M
for i in range(N):
    for j in range(M):
        if arr[i][j]=='L':
            for dir_num in range(8):
                nr1,nr2=i+dr[dir_num],i+2*dr[dir_num]
                nc1,nc2=j+dc[dir_num],j+2*dc[dir_num]
                if inrange(nr1,nc1) and inrange(nr2,nc2):
                    if arr[nr1][nc1]=='E' and arr[nr2][nc2]=='E':
                        count+=1
print(count)


        