n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
D={'R':0,'D':1,'U':2,'L':3}
d_num=D[d]
dc=[1,0,0,-1]
dr=[0,1,-1,0]
for i in range(t):
    nr=r+dr[d_num]
    nc=c+dc[d_num]
    if nc<1 or nc>n or nr<1 or nr>n:
        d_num=3-d_num
    else:
        r=r+dr[d_num]
        c=c+dc[d_num]
print(r,c)