n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(n):
    for j in range (n-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
for i in range(n):
    print(arr[i],end=' ')
