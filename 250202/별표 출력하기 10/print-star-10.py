n=int(input())
counteven=countodd=0
for i in range(2*n):
    if i%2==0:
        counteven+=1
        print('* '*counteven)
    else:
        countodd+=1
        print('* '*(n-countodd+1))
#print(counteven,countodd)
'''
for i in range(n,2*n):
    if i%2!=0:
        
        print('* '*(counteven))
        counteven-=1
    else:
        
        print('* '*(i+countodd))
        countodd+=1'''
        