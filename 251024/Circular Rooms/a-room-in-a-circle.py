n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
dist=[]
for i in range(n):
    prod=0
    for j in range(n):
        
        if j!=i:
            steps=(j-i)%5
            prod+=abs(a[j]*steps)
    dist.append(prod)
print(min(dist))
