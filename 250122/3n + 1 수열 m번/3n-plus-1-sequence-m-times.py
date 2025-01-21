n=int(input())
for i in range(n):
    count=0
    num=int(input())
    while(num>1):
        if num%2==0:
            num//=2
            count+=1
        else:
            num=num*3+1
            count+=1
        
    print(count)
    