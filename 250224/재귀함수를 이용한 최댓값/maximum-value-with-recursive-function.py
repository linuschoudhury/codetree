n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
index=0

def findmax(arr,index,largest):
    if index>=len(arr):
        return largest
    largest=max(arr[index],largest)
    return findmax(arr,index+1,largest)
print(findmax(arr,index,arr[0]))
    