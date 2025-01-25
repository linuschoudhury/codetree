n,m=map(int,input().split())
#print(m,n)
arr=list(map(int,input().split()))
count=0
for i in range(n):
    if arr[i]==m:
        count+=1
print(count) 