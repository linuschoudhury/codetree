arr=list(map(int,input().split()))
arr2=[]
for i in range(len(arr)):
    if arr[i]==0:
        break
    arr2.append((arr[i]//10)*10)
    #print(arr2[i],end=' ')

for i in range(100,0,-10):
    count=0
    for j in range(len(arr2)):
        if i==arr2[j]:
            count+=1
    print("%d - %d"%(i,count))

