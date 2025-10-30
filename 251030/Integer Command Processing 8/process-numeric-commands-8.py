N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_front":
        A.insert(0,int(line[1]))
    elif line[0]=='push_back':
        A.append(int(line[1]))
    

# Please write your code here.
    elif line[0] =='pop_front':
        print(A[0])
        A.pop(0)
    elif line[0]=='pop_back':
        print(A[-1])
        A.pop(len(A)-1)
    elif line[0]=='size':
        print(len(A))
    elif line[0]=='empty':
        print(1 if len(A)==0 else 0)
    elif line[0]=='front':
        print(A[0])
    else:
        print(A[-1])
    