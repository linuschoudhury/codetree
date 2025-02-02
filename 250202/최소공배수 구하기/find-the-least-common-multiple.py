n, m = map(int, input().split())

# Write your code here!
def lcm(a,b):
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
            multiple=i
            break
    print(multiple)
lcm(n,m)