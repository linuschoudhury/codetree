a, b, c = map(int, input().split())

# Please write your code here.
#print(a,b,c)

a1=a-11
b1=b-11
c1=c-11
result=c1+(b1*60)+(a1*24*60)
if result<0:
    print(-1)
else:
    print(result)