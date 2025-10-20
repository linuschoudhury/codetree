N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
# Please write your code here.
dir_dict={'N':0,'E':1,'S':2,'W':3}
x=y=0
count=0
found=False
for i in range(N):
    if found:
        break
    dir_num=dir_dict[dir[i]]
    for j in range(dist[i]):
        x+=dx[dir_num]
        y+=dy[dir_num]
        count+=1
        if x==0 and y==0:
            print(count)
            found=True
            break
if not found:
    print(-1)

    


    