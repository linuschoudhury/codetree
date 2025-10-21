n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
B=[0]*n

for i in range(n):
    total=0
    for j in range(n):
        total+=(abs(j-i))*A[j]
    B[i]=total
print(min(B))

    