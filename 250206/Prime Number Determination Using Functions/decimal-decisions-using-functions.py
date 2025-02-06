a, b = map(int, input().split())

# Write your code here!
def sumprime(x,y):
    arr=[]
    for i in range(x,y+1):
        cnt=0
        for j in range(1,i):
            
            if i%j==0:
                cnt+=1
        if cnt==1:
            arr.append(i)
    return sum(arr)
print(sumprime(a,b))
