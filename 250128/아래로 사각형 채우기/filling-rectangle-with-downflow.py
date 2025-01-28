n=int(input())

for i in range(n):
    count=1+i
    for j in range(n):
        print(count+j*n,end=' ')
        #count=count+j*n
    print()
