n=int(input())
count=0
def gaga(n):
    global count
    if n==1:
        return 0
    if n%2==0:
        count+=1
        gaga(n/2)
        
    else:
        count+=1
        gaga(n//3)
    return count
print(gaga(n))