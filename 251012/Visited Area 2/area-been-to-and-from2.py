n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
arr=[0]*10000
curr=5000
for i in range(n):
    if dir[i]=='R':
        for j in range(x[i]):
            arr[curr+j+1]+=1
            
        curr=curr+x[i]
        
        
    if dir[i]=='L':
        for j in range(x[i]):
            arr[curr-(j+1)]+=1
            
        curr=curr-x[i]
freq_dict = {}
for num in arr:
    if num in freq_dict:
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1

print(freq_dict[2])


        

