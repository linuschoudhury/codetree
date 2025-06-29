N, B = map(int, input().split())

# Please write your code here.
total=[]
while N>0:
    a=str(N%B)
    N=N//B
    total.append(a)
print(''.join(reversed(total)))

