n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
maxsum=0
for i in range(n-k+1):
    
    total=0
    for j in range(i,i+k):
        total+=(arr[j])
    maxsum=max(total,maxsum)
print(maxsum)