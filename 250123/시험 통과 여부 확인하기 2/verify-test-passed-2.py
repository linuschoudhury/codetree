n=int(input())
count=0
for i in range(n):
    avg=0
    marks=list(map(int,input().split()))
    avg=sum(marks)/4
    
    
    if avg>=60:
        print('pass')
        count+=1
    else:
        print('fail')
print(count)
