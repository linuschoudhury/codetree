a = input()

# Please write your code here.
size=len(a)
b=list(a)
for i in range(size):
    b[i]=int(b[i])
for i in range(size):
    if b[i]==0:
        b[i]=1
        break
total=0
a=int(a)
for i in range(size):
    total+=(b[i]*(2**(size-i-1)))

print(total)