n=int(input())
arr=[[' ']*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j%2==0:
            arr[0][j]='*'
        else:
            if j>=i:
                arr[i][j]='*'
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()
