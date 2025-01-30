n=int(input())
curr=1
arr=[[0] * n for _ in range(n)]
for j in range(n-1,-1,-1):
    if (n-j)%2==1:
        for i in range(n-1,-1,-1):
            arr[i][j]=curr
            curr+=1
    else:
        for i in range(n):
            arr[i][j]=curr
            curr+=1
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()
        