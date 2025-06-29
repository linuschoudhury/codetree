n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
array=[0]*100
for i in range(len(segments)):
    for j in range(segments[i][0]-1,segments[i][1]):
        array[j]+=1
print(max(array))

