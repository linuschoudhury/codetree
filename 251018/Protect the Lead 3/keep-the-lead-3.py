N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
time=sum(t)
A=[]
B=[]
for i in range(N):
    for j in range(t[i]):
        A.append(v[i])
for i in range(M):
    for j in range(t2[i]):
        B.append(v2[i])
#print(A)
#print(B)
totalA=totalB=0
lead=[]
for i in range(time):
    totalA+=A[i]
    totalB+=B[i]
    #print(totalA,totalB)
    if totalA>totalB:
        current_lead='A'
    elif totalB>totalA:
        current_lead='B'
    else:
        current_lead='AB'
    lead.append(current_lead)
#print(lead)
count=1
for i in range(1,len(lead)):
    if lead[i-1]!=lead[i]:
        count+=1
print(count)
