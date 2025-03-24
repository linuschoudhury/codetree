import sys
n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
minimum=-sys.maxsize-1
n=len(nums)//2
for i in range(n):
    minimum=max(minimum,nums[i]+nums[2*n-i-1])
print(minimum)




