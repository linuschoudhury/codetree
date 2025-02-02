n, m = map(int, input().split())

# Write your code here!
def gcd(a,b):
    for i in range(1,min(a+1,b+1)):
        if a%i==0 and b%i==0:
            answer=i 
    print(answer)
gcd(n,m)
