arr=list(map(int,input().split()))
#print(arr)
arr2=list()
for i in range(len(arr)):
    if arr[i]==0:
        break
    arr2.append(arr[i])
    #print(arr2[i],end=' ')
for i in range(len(arr2)-1,-1,-1):
    print(arr2[i],end=' ')
    