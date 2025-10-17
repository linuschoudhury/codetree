n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
time=max(sum(t),sum(t_b))
A=[]
B=[]
posA,posB=0,0
for i in range(n):
    if d[i]=='L':
        for j in range(t[i]):
            posA-=1
            A.append(posA)
    else:
        for j in range(t[i]):
            posA+=1
            A.append(posA)
for i in range(m):
    if d_b[i]=='L':
        for j in range(t_b[i]):
            posB-=1
            B.append(posB)
    else:
        for j in range(t_b[i]):
            posB+=1
            B.append(posB)

for i in range(time):
    if sum(t)<time:
        for j in range(sum(t),time):
            A.append(A[-1])
    elif sum(t_b)<time:
        for j in range(sum(t_b),time):
            B.append(B[-1])  
count=0
for i in range(1,time):
    if A[i-1]!=B[i-1] and A[i]==B[i]:
        count+=1
print(count)   

