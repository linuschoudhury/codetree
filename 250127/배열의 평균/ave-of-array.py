arr=[]
for i in range(2):
    row=list(map(int,input().split()))
    arr.append(row)
for i in range(2):
    print("%.1f"%(sum(arr[i])/4),end=' ')
print()
columnavg=[(arr[0][i]+arr[1][i])/2 for i in range(4)]
for i in range(4):
    print(columnavg[i],end=' ')
print()
total=0
for i in range(2):
    for j in range(4):
        total+=arr[i][j]

print("%.1f"%(total/8))


