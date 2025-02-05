a, b = map(int, input().split())

# Write your code here!
def multiples(x,y):
    cnt=0
    arr=[]
    for i in range(x,y+1):
        if i%3==0:
            cnt+=1
            arr.append(i)
        elif '3' in str(i) or '6' in str(i) or '9' in str(i):
            cnt+=1
            arr.append(i)
    return cnt


print(multiples(a,b))
