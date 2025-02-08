a, b = map(int, input().split())

# Write your code here!
def whole(x,y):
    count=0
    for i in range(x,y+1):
        if i%2==0:
            pass
        elif i%10==5:
            pass
        elif i%3==0 and i%9!=0:
            pass
        else:
            count+=1
    return count
print(whole(a,b))