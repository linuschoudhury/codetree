binary = input()

# Please write your code here.
x=0
dec=0
size=len(binary)
binary=int(binary)
for i in range(size):
    x=binary%10
    dec=dec+(x*(2**i))
    binary//=10
    #print(x)
print(dec)
    
