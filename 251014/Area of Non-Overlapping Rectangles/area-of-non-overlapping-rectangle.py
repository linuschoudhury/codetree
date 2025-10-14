x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
offset=1000
rects=[]
dic={}
for i in range(3):
    s=set()
    for j in range(x1[i]+offset,x2[i]+offset):
        for k in range(y1[i]+offset,y2[i]+offset):
            rects.append([j,k])
            t=tuple((j,k))
            dic[t]=i
            
count = sum(1 for v in dic.values() if v == 0)+sum(1 for v in dic.values() if v == 1)

print(count)