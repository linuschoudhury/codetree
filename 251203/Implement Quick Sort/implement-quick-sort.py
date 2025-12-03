n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def split(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        split(arr,low,pivot-1)
        split(arr,pivot+1,high)

split(arr,0,n-1)
print(' '.join(map(str,arr)))