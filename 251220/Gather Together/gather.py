n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
minsum=float('inf')
for i in range(n):
    sum=0
    for j in range(n):
        sum+=A[j]*abs(i-j)
    minsum=min(sum,minsum)
print(minsum)

