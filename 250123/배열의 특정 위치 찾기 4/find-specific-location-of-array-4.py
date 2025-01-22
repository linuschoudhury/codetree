arr=list(map(int,input().split()))
count=0
total=0
for i in range(len(arr)):
    if arr[i]%2==0:
        if arr[i]==0:
            break
        count+=1
        total+=arr[i]
        #print(arr[i])
print("%d %d"%(count,total))