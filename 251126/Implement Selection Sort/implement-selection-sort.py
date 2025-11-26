n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    minindex=i
    for j in range(i+1,n):
        if arr[minindex]>arr[j]:
            minindex=j
    arr[minindex],arr[i]=arr[i],arr[minindex]
    print(arr[i],end=' ')