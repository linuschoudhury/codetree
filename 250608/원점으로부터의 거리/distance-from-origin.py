n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
for i in range(n):
    
    dist=abs(points[i][1][0])+abs(points[i][1][1])
    
points.sort(key=lambda x:(abs(x[1][0])+abs(x[1][1])))
for i in range(n):
    print(points[i][0]+1)