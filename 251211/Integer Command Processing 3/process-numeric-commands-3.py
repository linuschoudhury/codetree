n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
from collections import deque
class Queue:
    def __init__(self):
        self.dq=deque()
    def push_back(self,item):
        self.dq.append(item)
    def push_front(self,item):
        self.dq.appendleft(item)
    def empty(self):
        if not self.dq:
            return 1
        else:
            return 0
    def size(self):
        if not self.dq:
            return 0
        return len(self.dq)
    def pop_front(self):
        if not self.dq:
            return 0
        return self.dq.popleft()
    def pop_back(self):
        if not self.dq:
            return 0
        return self.dq.pop()
    def front(self):
        if not self.dq:
            return 0
        return self.dq[0]
    def back(self):
        if not self.dq:
            return 0
        return self.dq[-1]
q=Queue()
for i in range(n):
    if cmd[i]=='push_back':
        q.push_back(num[i])
    elif cmd[i]=='push_front':
        q.push_front(num[i])
    elif cmd[i]=='pop_front':
        print(q.pop_front())
    elif cmd[i]=='pop_back':
        print(q.pop_back())
    elif cmd[i]=='front':
        print(q.front())
    elif cmd[i]=='back':
        print(q.back())
    elif cmd[i]=='empty':
        print(q.empty())
    elif cmd[i]=='size':
        print(q.size())
    
