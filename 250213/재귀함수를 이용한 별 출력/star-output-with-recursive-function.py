n = int(input())

# Write your code here!
def printstar(n):
    if n==0:
        return
    printstar(n-1)
    print('*'*n)
printstar(n)