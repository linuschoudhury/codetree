a, b = map(int, input().split())

# Write your code here!
def doThis(x,y):
    if x==min(x,y):
        newx=x+10
    else:
        newx=x*2
    if y==min(x,y):
        newy=y+10
    else:
        newy=y*2
    print(newx,newy)
doThis(a,b)
    
