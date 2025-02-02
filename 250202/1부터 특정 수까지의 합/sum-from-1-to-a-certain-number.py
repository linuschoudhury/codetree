n = int(input())

# Write your code here!
def total(a):
    total=0
    for i in range(a+1):
        total+=i
    return total//10
print(total(n))

    