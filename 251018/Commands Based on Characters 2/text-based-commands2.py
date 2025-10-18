dirs = input()

# Please write your code here.
x=0
y=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
dir_num=1
for i in range(len(dirs)):
    if dirs[i]=='L':
        if dir_num==0:
            dir_num=1
        elif dir_num==1:
            dir_num=2
        elif dir_num==2:
            dir_num=3
        else:
            dir_num=0
    elif dirs[i]=='R':
        if dir_num==0:
            dir_num=3
        elif dir_num==3:
            dir_num=2
        elif dir_num==2:
            dir_num=1
        else:
            dir_num=0
    else:
        x+=dx[dir_num]
        y+=dy[dir_num]
print(x,y)
