arr=list(map(int,input().split()))
for i in range(1,7):
    count=0
    for j in range(10):
        if arr[j] == i:
            count+=1
    print("%d - %d"%(i,count))
            
