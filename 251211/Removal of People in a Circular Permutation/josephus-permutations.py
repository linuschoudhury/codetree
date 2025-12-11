n, k = map(int, input().split())

# Please write your code here.
from collections import deque
class Queue:
    def __init__(self):
        self.dq=deque()
    def push(self,item):
        self.dq.append(item)
    def pop(self):
        if len(self.dq)==0:
            raise Exception('Queue is empty')
        return self.dq.popleft()
    def __getitem__(self,index):
        return self.dq[index]
    def empty(self):
        return not self.dq
    def size(self):
        return len(self.dq)
q=Queue()
for i in range(n):
    q.push(i+1)

while not q.empty():
    for i in range(k-1):
        q.push(q.pop())
    print(q.pop(),end=' ')


