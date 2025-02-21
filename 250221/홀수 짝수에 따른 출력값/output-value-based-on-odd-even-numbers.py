N = int(input())

# Write your code here!
def fact(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return n+fact(n-2)
print(fact(N)) 