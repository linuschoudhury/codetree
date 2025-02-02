n=int(input())
arr=[[' ']*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            arr[i][j]='*'
        elif i>j:
            arr[i][j]='*'
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()
        