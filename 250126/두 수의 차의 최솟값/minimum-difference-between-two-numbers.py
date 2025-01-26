n=int(input())
arr=list(map(int,input().split()))
result=100
for i in range(n-1):
    result=min(result,arr[i+1]-arr[i])
print(result)
