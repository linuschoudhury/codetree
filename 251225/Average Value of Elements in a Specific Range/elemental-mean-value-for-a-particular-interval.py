n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
count=0
for i in range(n):
    for j in range(i+1,n+1):
        t=arr[i:j]
        avg=sum(t)/len(t)
        if avg in t:
            count+=1
        #print(t,avg,avg in t)
print(count)

    