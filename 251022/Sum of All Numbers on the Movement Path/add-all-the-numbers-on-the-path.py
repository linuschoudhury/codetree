N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
start=N//2

dr=[-1,0,1,0]
dc=[0,-1,0,1]
dir_num=0
r=c=start
count=board[r][c]
def inrange(x,y):
    return 0<=x<N and 0<=y<N
for i in range(T):
    if str[i]=='L':
        dir_num=(dir_num+1)%4
    elif str[i]=='R':
        dir_num=(dir_num-1)%4
    else:
        nr=r+dr[dir_num]
        nc=c+dc[dir_num]
        if inrange(nr,nc):
            r=r+dr[dir_num]
            c=c+dc[dir_num]
            count+=board[r][c]
print(count)





