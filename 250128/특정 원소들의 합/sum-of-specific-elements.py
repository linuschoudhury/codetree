arr=[]
for i in range(4):
    row=list(map(int,input().split()))
    arr.append(row)
total=0
for i in range(4):
    for j in range(4):
        if i>=j:
            total+=arr[i][j]
print(total)
