n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
for num in nums:
    print(num,end=' ')
print()
nums.sort(reverse=True)
for num in nums:
    print(num,end=' ')
