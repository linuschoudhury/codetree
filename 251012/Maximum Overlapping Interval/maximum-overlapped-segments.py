n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr=[0]*201
for a,b in segments:
    a+=100
    b+=100
    for j in range(a,b):
        arr[j]+=1
print(max(arr))
    