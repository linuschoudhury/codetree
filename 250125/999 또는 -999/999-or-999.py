arr=list(map(int,input().split()))
arr1=[]
for i in range(len(arr)):
    if arr[i]==999 or arr[i]==-999:
        break
    else:
        arr1.append(arr[i])
print(max(arr1),min(arr1))