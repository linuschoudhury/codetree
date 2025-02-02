n=int(input())
counteven=n
countodd=1
for i in range(2*n):
    if i%2==0:
        print('* '*counteven)
        counteven-=1
    else:
        print('* '*countodd)
        countodd+=1