n, m = map(int, input().split())

# Write your code here!
cnt=0
arr = [[0 for _ in range(m)] for _ in range(n)]
for j in range(m):
    
    if j%2==0:
        for i in range(n):
            arr[i][j]=cnt
            #print(('(%d,%d)'%(i,j)),end=' ')
            #print(cnt)
            cnt+=1
    else:
        cnt+=3
        for i in range(n):
            arr[i][j]=cnt
            #print(('(%d,%d)'%(i,j)),end=' ')
            #print(cnt)
            cnt-=1
#print(arr)
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()







