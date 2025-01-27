arr1=[]
arr2=[]

for i in range(3):
    row1=list(map(int,input().split()))
    arr1.append(row1)
input().strip()
for j in range(3):
    row2=list(map(int,input().split()))
    arr2.append(row2)
for i in range(3):
    for j in range(3):
        print(arr1[i][j]*arr2[i][j],end=' ')
    print()

    
