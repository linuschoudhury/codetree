n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x=y=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
for i in range(n):
    for j in range(dist[i]):
        if dir[i]=='E':
            x+=dx[0]
            y+=dy[0]
        elif dir[i]=='N':
            x+=dx[1]
            y+=dy[1]
        elif dir[i]=='W':
            x+=dx[2]
            y+=dy[2]
        else:
            x+=dx[3]
            y+=dy[3]
print(x,y)
