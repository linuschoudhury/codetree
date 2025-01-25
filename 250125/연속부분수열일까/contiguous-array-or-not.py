n1,n2=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
strA=''
strB=''
for i in range(len(A)):
    strA+=str(A[i])
for i in range(len(B)):
    strB+=str(B[i])
if strB in strA:
    print('Yes')
else:
    print('No')
