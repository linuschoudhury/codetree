n1,n2=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
intA=0
intB=0
for i in range(len(A)):
    intA=intA*10+A[i]
for i in range(len(B)):
    intB=intB*10+B[i]
strA=str(intA)
strB=str(intB)
if strB in strA:
    print('Yes')
else:
    print('No')
