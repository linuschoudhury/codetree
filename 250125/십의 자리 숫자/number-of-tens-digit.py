arr=list(map(int,input().split()))
for i in range(1,10):
    count=0
    for j in range(len(arr)):
        if arr[j]//10==i:
            count+=1
        if arr[j]==0:
            break
    print("%d - %d"%(i,count))