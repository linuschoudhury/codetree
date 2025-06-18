a, b, c = map(int, input().split())

# Please write your code here.
#print(a,b,c)
if a<11 or b<11 or c<11:
    print(-1)
else:
    a1=a-11
    b1=b-11
    c1=c-11
    result=c1+(b1*60)+(a1*24*60)
    print(result)