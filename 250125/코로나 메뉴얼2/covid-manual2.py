countA=0
countB=0
countC=0
countD=0
result=''
for i in range(3):
    arr=input().split()
    if arr[0] == 'Y' and int(arr[1])>=37:
        countA+=1
    elif arr[0] == 'N' and int(arr[1])>=37:
        countB+=1
    elif arr[0] == 'Y' and int(arr[1])<=37:
        countC+=1
    elif arr[0] == 'N' and int(arr[1])<=37:
        countD+=1
result='E' if countA>=2 else ''
print("%d %d %d %d %s"%(countA,countB,countC,countD,result))
