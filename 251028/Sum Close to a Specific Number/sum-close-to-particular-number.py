N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here
fucks=[]
for i in range(N):
    for j in range(N):
        total=0
        if i!=j:
            total=sum(arr)-arr[i]-arr[j]
            total=abs(total-S)
            fucks.append(total)
        
print(min(fucks))

        


    
    


