n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
colordict={}
cur=0
for i in range(n):
    if dir[i]=='L':
        for j in range(cur,cur-x[i],-1):
            colordict[j]='W'
        cur=cur-x[i]+1
    else:
        for j in range(cur,cur+x[i]):
            colordict[j]='B'
        cur=cur+x[i]-1
whites=blacks=0
for k,v in colordict.items():
    whites+=v.count('W')
    blacks+=v.count('B')
print(whites,blacks)
            