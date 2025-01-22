arr=list(map(int,input().split()))
#print(arr)
for i in range(len(arr)-1,-1,-1):
    if arr[i]!=0:
        print(arr[i],end=' ')