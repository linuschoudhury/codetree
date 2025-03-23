n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()
flag=True
if len(A)!=len(B):
    flag=False
else:
    for i in range(len(A)):
        if A[i]!=B[i]:
            flag=False
if flag==False:
    print('No')
else:
    print('Yes')

