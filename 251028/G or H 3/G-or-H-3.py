n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
arr=[0]*max(x)
for i in range(n):
    arr[x[i]-1]=c[i]
maxcount=0
for i in range(len(arr)-k):
    count=0
    for j in range(i,i+k+1):
        if arr[j]=='G':
            count+=1
        elif arr[j]=='H':
            count+=2
    maxcount=max(count,maxcount)
print(maxcount)
