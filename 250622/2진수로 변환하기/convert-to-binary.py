n = int(input())

# Please write your code here.
binary=[]
if n==0:
    print(0)
while n>0:
    binary.append(n%2)
    n=n//2
for digit in binary[::-1]:
    print(digit,end='')
