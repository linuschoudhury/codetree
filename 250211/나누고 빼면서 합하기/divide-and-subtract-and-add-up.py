n, m = map(int, input().split())
A = list(map(int, input().split()))

# Write your code here!
def whatever(A):
    total=0
    global n,m
    j=m+1
    while j>1:
        if j%2!=0:
            j-=1
        else:
            j//=2
        total+=A[j-1]
    print(total)
        

whatever(A)