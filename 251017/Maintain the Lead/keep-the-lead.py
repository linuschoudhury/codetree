n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)
# Please write your code here.
time=sum(t)
A=[]
B=[]
C=[]
count=0
sumA,sumB=0,0
for i in range(len(t)):
    for j in range(t[i]):
        A.append(v[i])
for i in range(len(t2)):
    for j in range(t2[i]):
        B.append(v2[i])
for i in range(time):
    sumA+=A[i]
    sumB+=B[i]
    if sumA>sumB:
        C.append('A')
    elif sumA<sumB:
        C.append('B')
for i in range(1,len(C)):
    if C[i-1]!=C[i]:
        count+=1
print(count)



