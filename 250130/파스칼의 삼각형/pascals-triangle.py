n=int(input())
arr=[[1]*(i+1) for i in range(n)]

for i in range(2,n):
    for j in range(1,i):
        arr[i][j]=arr[i-1][j]+arr[i-1][j-1]
for i in range(n):
    for j in range(i+1):
        print(arr[i][j],end=' ')
    print()
                
