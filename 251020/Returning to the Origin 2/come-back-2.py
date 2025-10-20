commands = input()

# Please write your code here
x=y=0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
pointing=0
count=0
found=False
for i in range(len(commands)):
    if commands[i]=='L':
        pointing=(pointing-1)%4
        count+=1
    if commands[i]=='R':
        pointing=(pointing+1)%4
        count+=1
    else:
        x+=dx[pointing]
        y+=dy[pointing]
        count+=1
    if x==0 and y==0:
        found=True
        print(count)
        break
if not found:
    print(-1)
