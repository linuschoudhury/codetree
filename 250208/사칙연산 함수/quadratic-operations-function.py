a, o, c = input().split()
a = int(a)
c = int(c)

# Write your code here!
def add(x,y):
    return a+c
def subtract(x,y):
    return a-c
def multiply(x,y):
    return a*c
def divide(x,y):
    return a//c
if o=='+':
    print('%d + %d = %d'%(a,c,add(a,c)))
elif o=='-':
    print('%d - %d = %d'%(a,c,subtract(a,c)))
elif o=='*':
    print('%d * %d = %d'%(a,c,multiply(a,c)))
elif o=='/':
    print('%d / %d = %d'%(a,c,divide(a,c)))
else:
    print('False')

