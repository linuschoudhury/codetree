n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max1=max2=0

for i in range(n):
    for j in range(n-2):
        total1= arr[i][j]+arr[i][j+1]+arr[i][j+2]
        for k in range(n):
            for l in range(n-2):
                overlaps = (i == k) and (l <= j+2) and (l+2 >= j)
                if not overlaps:
                    total2=arr[k][l]+arr[k][l+1]+arr[k][l+2]
                    max1=max(max1,total1+total2)
print(max1)