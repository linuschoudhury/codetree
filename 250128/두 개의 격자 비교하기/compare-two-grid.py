n,m=map(int,input().split())
arr1=[]
arr2=[]
for i in range(n):
    row1=list(map(int,input().split()))
    arr1.append(row1)

for j in range(n):
    row2=list(map(int,input().split()))
    arr2.append(row2)
for i in range(n):
    for j in range(m):
        print(0 if arr1[i][j]==arr2[i][j] else 1,end=' ')
    print()