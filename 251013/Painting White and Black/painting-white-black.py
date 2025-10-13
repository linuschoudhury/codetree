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
            if j not in colordict:
                colordict[j]=[]
            colordict[j].append('W')
        cur=cur-x[i]+1
    else:        
        for j in range(cur,cur+x[i]): 
            if j not in colordict:
                colordict[j]=[]
            colordict[j].append('B')
        cur=cur+x[i]-1

greycount=whitecount=blackcount=0
for k,v in colordict.items():
    if v.count('W')>=2 and v.count('B')>=2:
        greycount+=1
    elif v[-1]=='W':
        whitecount+=1
    elif v[-1]=='B':
        blackcount+=1
print(whitecount,blackcount,greycount)

