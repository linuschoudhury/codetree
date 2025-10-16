n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
count=0
maxcount=0
for i in range(n):
    if arr[i]>t:
        count+=1
    else:
        count=0
    maxcount=max(count,maxcount)
print(maxcount)
