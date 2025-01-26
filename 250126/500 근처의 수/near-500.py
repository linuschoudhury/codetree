arr=list(map(int,input().split()))
largest = 0
smallest= 1000
for i in range(len(arr)):
    if arr[i]<500:
        largest = max(largest,arr[i])
    elif arr[i]>500:
        smallest=min(smallest,arr[i])
print(largest, smallest)
