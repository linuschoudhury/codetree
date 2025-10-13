x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
A={}

for j in range(x1[0],x2[0]):
    for k in range(y1[0],y2[0]):
        
        t=tuple((j,k))
       
        if t not in A:
            A[t]=1
        else:
            A[t]+=1
B={}
for j in range(x1[1],x2[1]):
    for k in range(y1[1],y2[1]):
        t=tuple((j,k))
        if t not in B:
            B[t]=1
        else:
            B[t]+=1
C={}
for j in range(x1[2],x2[2]):
    for k in range(y1[2],y2[2]):
        t=tuple((j,k))
        if t not in C:
            C[t]=1
        else:
            C[t]+=1
onlyA=len([k for k in A if k not in C])
onlyB=len([k for k in B if k not in C])
print(onlyA+onlyB)