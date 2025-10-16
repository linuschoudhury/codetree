n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
A=[]
B=[]
posA,posB=0,0
totalTa=0
totalTb=0
for i in range(n):
    totalTa+=t[i]
    for j in range(t[i]):
        if d[i]=='R':
            posA+=1
            A.append(posA)
        else:
            posA-=1
            A.append(posA)
for i in range(m):
    totalTb+=t2[i]
    for j in range(t2[i]):
        if d2[i]=='R':
            posB+=1
            B.append(posB)
        else:
            posB-=1
            B.append(posB)

for i in range(totalTa):
    if A[i]==B[i]:
        print(i+1)
        break
else:
    print(-1)


