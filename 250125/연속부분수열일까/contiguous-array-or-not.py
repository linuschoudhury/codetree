n1,n2=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
count=0
if B[0] in A:
    start=A.index(B[0])
    for i in range(start,start+len(B)):
        if A[i]==B[i-start]:
            count+=1
        else:
            break
        #print(B[])
if count==len(B):
    print('Yes')
else:
    print('No')