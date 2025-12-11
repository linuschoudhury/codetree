N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.

from collections import deque
class Queue:
    def __init__(self):
        self.dq=deque()
    def push(self,item):
        self.dq.append(item)
    def size(self):
        return len(self.dq)
    def empty(self):
        if not self.dq:
            return 1
        else:
            return 0
    def front(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq[0]
    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.dq.popleft()
q=Queue()
for i in range(N):
    if command[i]=='push':
        q.push(A[i])
    elif command[i]=='size':
        print(q.size())
    elif command[i]=='empty':
        print(q.empty())
    elif command[i]=='front':
        print(q.front())
    elif command[i]=='pop':
        print(q.pop())
