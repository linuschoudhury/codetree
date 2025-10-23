n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
nums=[[0]*5 for _ in range(n)]
for i in range(n):
    temp=arr[i]
    for j in range(5):       
        num=temp%10
        temp=temp//10
        nums[i][4-j]=num
sums=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (nums[i][4]+nums[j][4]+nums[k][4])<10 and (nums[i][3]+nums[j][3]+nums[k][3])<10 and (nums[i][2]+nums[j][2]+nums[k][2])<10 and (nums[i][1]+nums[j][1]+nums[k][1])<10 and (nums[i][0]+nums[j][0]+nums[k][0])<10:
                sums=arr[i]+arr[j]+arr[k]
print(sums)




    