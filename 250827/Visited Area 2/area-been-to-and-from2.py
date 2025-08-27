n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
storage=[]
curr=0
for j in range(len(dir)):
    for k in range(x[j]):
        if dir[j]=='R':
            
            storage.append((curr,curr+1))
            curr=curr+1
        else:
            
            storage.append((curr,curr-1))
            curr=curr-1

final={}
for edge in storage:
    edge=(min(edge[0], edge[1]), max(edge[0], edge[1])) 
    if edge in final:
        final[edge]+=1
    else:
        final[edge]=1
total=0
for edge, count in final.items():
    if count>1:
        total+=1
print(total)


        


