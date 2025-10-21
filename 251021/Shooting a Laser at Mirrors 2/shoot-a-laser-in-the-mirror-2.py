n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.

side=(k-1)//n
pos=(k-1)%n
if side==0:
    r,c=-1,pos
    dr,dc=1,0
elif side==1:
    r,c=pos,n
    dr,dc=0,-1
elif side==2:
    r,c=n,n-1-pos
    dr,dc=-1,0
else:
    r,c=n-1-pos,-1
    dr=0,1
reflections=0
while True:
    r+=dr
    c+=dc
    if r<0 or r>=n or c<0 or c>=n:
        break
    reflections+=1
    mirror=grid[r][c]
    if mirror=='\\':
        dr,dc=dc,dr
    else:
        dr,dc=-dc,-dr
print(reflections)
