n=int(input())

def printthis(n):
    if n==0:
        return
    print(n,end=' ')
    printthis(n-1)
    print(n,end=' ')
printthis(n)