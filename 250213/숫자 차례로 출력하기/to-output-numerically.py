n = int(input())

# Write your code here!
def first(n):
    if n==0:
        return
    
    first(n-1)
    print(n,end=' ')
first(n)
print()
def second(n):
    if n==0:
        return
    print(n,end=' ')
    second(n-1)
    
second(n)
