n=int(input())
for i in range(2,n+1):
    count=0
    isprime=0
    for j in range(2,i):
        if i%j==0:
            count+=1
    if count==0:
        #isprime+=1
        print(i,end= ' ')
#print(isprime)