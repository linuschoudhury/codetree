N = input()

# Please write your code here.
N=int(N)
total=0
while N>0:
    for i in range(10):
        a=(N%10)*(2**i)
        total+=a
        N=N//10
total*=17
finbin=[]
while total>0:
    a=str(total%2)
    finbin.append(a)
    total=total//2
#print(finbin)
print(''.join(reversed(finbin)))


