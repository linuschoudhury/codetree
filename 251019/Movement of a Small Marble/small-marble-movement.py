n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
D = {'R':0, 'D':1, 'L':2, 'U':3}
d_num = D[d]

dr = [0, 1, 0, -1]  # row changes
dc = [1, 0, -1, 0]  # column changes

for _ in range(t+1):
    r += dr[d_num]
    c += dc[d_num]

    # bounce off walls
    if r == 0 and d_num == 3:  # U → D
        d_num = 1
    elif r == n-1 and d_num == 1:  # D → U
        d_num = 3

    if c == 0 and d_num == 2:  # L → R
        d_num = 0
    elif c == n-1 and d_num == 0:  # R → L
        d_num = 2

print(r, c)