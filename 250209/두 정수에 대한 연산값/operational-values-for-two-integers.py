a, b = map(int, input().split())

# Write your code here!
def doThis(x,y):
    if x==min(x,y):
        newx=x*2
    else:
        newx=x+25
    if y==min(x,y):
        newy=y*2
    else:
        newy=y+25
    print(newx,newy)
doThis(a,b)
    