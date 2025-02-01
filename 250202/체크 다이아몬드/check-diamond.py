n=int(input())
size=2*n-1
middle=size//2

for i in range(n):
    spaces=n-i-1
    stars=i+1
    print(spaces*' '+stars*'* ')

for i in range(n,2*n-1):
    spaces=i-n+1
    stars=2*n-i-1
    print(spaces*' '+stars*'* ')
print()