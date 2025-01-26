n = int(input())
price = list(map(int, input().split()))

# Write your code here!

profit=0
for i in range(n):
    for j in range(i+1,n):
        profit=max(profit,price[j]-price[i])
print(profit)