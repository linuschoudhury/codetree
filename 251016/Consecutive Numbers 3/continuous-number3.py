N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
poscount=0
negcount=0
maxcount=1
for i in range(N):
    if arr[i]<0:
        negcount+=1
        poscount=0
    else:
        poscount+=1
        negcount=0
    maxcount=max(maxcount,poscount,negcount)
print(maxcount)

