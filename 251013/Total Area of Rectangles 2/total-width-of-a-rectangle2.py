n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
offset=100
cells=[]
for i in range(n):
    for j in range(x1[i],x2[i]):
        for k in range(y1[i],y2[i]):
            cells.append([j,k])
celldict={}

for cell in cells:
    t=tuple(cell)
    if t not in celldict:
        celldict[t]=1
    else:
        celldict[t]+=1
print(len(celldict))
