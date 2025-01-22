arr=list(map(int,input().split()))
#print(arr)
count=0
sum=0
for i in range(len(arr)):
    if arr[i]<250:
        sum+=arr[i]
        count+=1
    else:
        break
print(sum,sum/count)