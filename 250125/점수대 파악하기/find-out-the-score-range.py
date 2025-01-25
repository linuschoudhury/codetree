arr=list(map(int,input().split()))
for i in range(len(arr)):
    arr[i]=(arr[i]//10)*10
for i in range(100,0,-10):
    count=0
    for j in range(len(arr)):
        if i==arr[j]:
            count+=1
    print("%d - %d"%(i,count))

