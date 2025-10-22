a = input()

# Please write your code here.
size=len(a)
b=[]
for num in a:
    b.append(int(num))
total=[]

for i in range(size):
    dec=0
    temp=b[i]
    if b[i]==0:
        b[i]=1
    else:
        b[i]=0
    for j in range(size):
        dec+=b[j]*(2**(size-j-1))
    total.append(dec)
    b[i]=temp
print(max(total))

    
