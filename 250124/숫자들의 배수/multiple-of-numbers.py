n=int(input())
count=0
for i in range(1,11):
    count+=1
    if n%5==0 and count==3:
        break
    print(n*i,end= ' ')