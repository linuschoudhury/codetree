arr=list(map(int,input().split()))
total=0
count=0
avg=0
for i in range(len(arr)):
    if arr[i]==0:
        break
    total+=arr[i]
    count+=1
avg=total/count
print("%d %.1f"%(total,avg))
