n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
import sys
mindist = sys.maxsize


for j in range(1,len(points)-1):
    path=points[:j]+points[j+1:]
    dist = 0
    for k in range(len(path)-1):
        dist=dist+(abs(path[k][0]-path[k+1][0])+abs(path[k][1]-path[k+1][1]))
    mindist=min(dist,mindist)
print(mindist)
