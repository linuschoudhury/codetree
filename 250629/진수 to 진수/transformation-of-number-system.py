a, b = map(int, input().split())
n = input()

# Please write your code here.
n=int(n)
total=0
i=0
while n>0:
    c=n%10
    total+=c*(a**i)
    #print(c,a**i,c*(a**i))
    i+=1
    n=n//10
    
#print(total)
fintotal=[]
while total>0:
    c=total%b
    fintotal.append(str(c))
    total=total//b
print(''.join(reversed(fintotal)))
