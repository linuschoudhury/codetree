n=int(input())
prod=1
def fact(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return fact(n-1)*n
print(fact(n))
    