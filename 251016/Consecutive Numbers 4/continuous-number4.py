n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
count=1
maxcount=1
for i in range(1,n):
    if arr[i-1]<arr[i]:
        count+=1
    else:
        count=1
    maxcount=max(count,maxcount)
print(maxcount)