n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
k=10
for pos in range(k-1,-1,-1):
    arr_new=[[] for _ in range(10)]
    for i in range(len(arr)):
        digit=(arr[i]//(10**pos))%10
        arr_new[digit].append(arr[i])
store_arr=[]
for i in range(10):
    for j in range(len(arr_new[i])):
        store_arr.append((arr_new[i][j]))
        
for num in store_arr:
    print(num, end=' ')