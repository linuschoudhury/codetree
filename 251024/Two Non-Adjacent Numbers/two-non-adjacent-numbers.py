n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
arr=[]
for i in range(n):
    
    for j in range(i+2,n):
        total=0
        total+=numbers[i]+numbers[j]
        arr.append(total)
print(max(arr))