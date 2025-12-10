N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def empty(self):
        if len(self.items)==0:
            return 1
        else:
            return 0
    def size(self):
        return len(self.items)
    def pop(self):
        if len(self.items)==0:
            return -1
        return self.items.pop()
    def top(self):
        if len(self.items)==0:
            raise Exception("Stack is empty")
        return self.items[-1]
stack=Stack()
for i in range(N):
    if command[i]=='push':
        stack.push(value[i])
    elif command[i]=='pop':
        print(stack.pop())
    elif command[i]=='size':
        print(stack.size())
    elif command[i]=='empty':
        print(stack.empty())
    elif command[i]=='top':
        print(stack.top())