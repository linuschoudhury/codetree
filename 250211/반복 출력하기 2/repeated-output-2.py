n = int(input())

# Write your code here!
def printstring(N):
    if N==0:
        return
    printstring(N-1)
    print('HelloWorld')
printstring(n)