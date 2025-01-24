n=int(input())
arr=[1,n]
i=2
x=1+n
print(1, n, end=' ')
while True:
    arr.append(arr[i-1]+arr[i-2])
    print(arr[i],end=' ')
    if arr[i]>100:
        break
    i+=1



    