n=int(input())

arr=list(map(int,input().split()))
result=[]
for i in range(1,10):
    count=0
    for j in range(n):
        if i == arr[j]:
            count+=1
    result.append(count)
    print(count)
    