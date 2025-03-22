n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def twonumbers(a,b):
    return abs(a*b)/gcd(a,b)
def recursivelcm(arr):
    if len(arr)==1:
        return arr[0]
    if len(arr)==2:
        return twonumbers(arr[0],arr[1])
    return twonumbers(arr[0],recursivelcm(arr[1:]))
print(int(recursivelcm(arr)))