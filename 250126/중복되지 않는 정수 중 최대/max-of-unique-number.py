n = int(input())
nums = list(map(int, input().split()))
larger=0
# Write your code here!
frequency={}
for num in nums:
    frequency[num]=frequency.get(num,0)+1
maxvalue=-1
for num,count in frequency.items():
    if count==1:
        maxvalue=max(maxvalue,num)
print(maxvalue)

