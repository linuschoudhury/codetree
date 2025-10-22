n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
dist=[]

for i in range(1,n):
    total=0
    for j in range(1,n):
        if i!=j:
            total+=abs(points[i][0]-points[i-1][0])+abs(points[i][1]-points[i-1][1])
    dist.append(total)
print(min(dist[1:-1]))
  

