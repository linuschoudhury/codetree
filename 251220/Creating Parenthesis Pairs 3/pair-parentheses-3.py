A = input()

# Please write your code here.
cnt=0
n=len(A)
for i in range(n):
    for j in range(i,n):
        if A[i]=='(' and A[j]==')':
            cnt+=1
print(cnt)