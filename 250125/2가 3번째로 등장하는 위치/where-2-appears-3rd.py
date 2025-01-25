n=int(input())
arr=list(map(int,input().split()))
count2=0
for i in range(n):
    if arr[i]==2:
        count2+=1
        if count2==3:
            break
print(i+1)