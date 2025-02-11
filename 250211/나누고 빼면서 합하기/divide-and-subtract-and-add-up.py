n, m = map(int, input().split())
A = list(map(int, input().split()))

# Write your code here!
def whatever(A):
    total=0
    global n,m
    j=m+1
    while m>=1:
        total+=A[m-1]
        print(m)
        if m%2!=0:
            m-=1
        else:
            m//=2
        
        
    print(total)
        

whatever(A)