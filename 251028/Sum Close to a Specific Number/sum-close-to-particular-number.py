N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
total=[0]*N
for i in range(N):
    total[i]=sum(arr[i:i+4])
    total[i]=abs(total[i]-S)
print(min(total))

    


