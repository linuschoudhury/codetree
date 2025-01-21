start, end = map(int, input().split())

# Write your code here!
div3=0

for i in range(start,end+1):
    count=0
    #print("i=%d"%i)
    for j in range(1,i):
        #print("j=%d"%j)
        if i%j==0:
            #print(i)
            #print(j)
            count+=1
        #print("count%d"%count)
    if count==2:
        #print(i)
        div3+=1
print(div3)
