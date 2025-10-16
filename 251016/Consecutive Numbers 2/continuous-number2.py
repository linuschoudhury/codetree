n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
count=1
maxcount=1
for i in range(n-1):
    if arr[i]==arr[i+1]:
        count+=1
    else:
        maxcount=max(count,maxcount)
        count=1

print(maxcount)
