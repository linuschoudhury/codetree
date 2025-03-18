n = int(input())

# Please write your code here.
count=0
def func(n):
    global count
    if n==1:
        print(count)
        return
    if n%2==0:
        count+=1
        return func(n/2)       
    if n%2==1:
        count+=1
        return func(n*3+1) 
    return False
#count+=1
func(n)