n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
offset=100
checked = [[0] * 2001 for _ in range(2001)]
for i in range(n):
    for j in range(x1[i],x2[i]):
        for k in range(y1[i],y2[i]):
            if i%2==0:
                checked[j][k]='R'
            else:
                checked[j][k]='B'
print(sum(row.count('B')for row in checked))

