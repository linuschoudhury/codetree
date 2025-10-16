N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
A=[0]*(N+1)
for i in range(len(student)):
    A[student[i]]+=1
    if A[student[i]]==K:
        break
else:
    print(-1)
print(student[i])



    