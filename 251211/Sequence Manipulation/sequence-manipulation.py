n = int(input())

# Please write your code here.
from collections import deque
q=deque()
for i in range(n):
    q.append(i+1)
while len(q)>1:
    q.popleft()
    front=q.popleft()
    q.append(front)
for i in range(len(q)):
    print(q[i])
    