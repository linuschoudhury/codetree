arr=list(map(int,input().split()))
total=0
avg=0
total3=0
count3=0
for i in range(10):
    if i%2!=0:
        total+=arr[i]
    if i%3==2:
        count3+=1
        total3+=arr[i]
        avg=total3/count3
print("%d %.1f"%(total,avg))