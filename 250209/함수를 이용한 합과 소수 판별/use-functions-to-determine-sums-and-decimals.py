a, b = map(int, input().split())

# Write your code here!
def evendigitprime(x,y):
    count=0
    arr=[]
    for i in range(x,y+1):
        isPrime=True
        for j in range(2,i):
            if i%j==0:
                isPrime=False
        i=str(i)
        digitSum=0
        for char in i:
            digitSum+=int(char)
        if isPrime==True and digitSum%2==0:
            arr.append(i)
            count+=1
    return count
print(evendigitprime(a,b))       


