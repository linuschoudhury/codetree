N = int(input())

# Please write your code here.
def func(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return func(n-1)+func(n//3)
print(func(N))