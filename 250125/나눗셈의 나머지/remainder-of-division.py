arr=input().split()
a,b=int(arr[0]),int(arr[1])
remarray=[]
while a>1:
    remarray.append(a%b)
    a=a//b
#print(remarray)

total=0
for i in range(10):
    count=0
    for j in range(len(remarray)):
        if i==remarray[j]:
            count+=1
    #print(i,count)
    total+=count**2
print(total)
    