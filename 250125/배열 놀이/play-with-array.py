n,q=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(q):
    qarr=list(map(int,input().split()))
    #print(qarr[1])
    #print(arr)
    #print(len(arr))
    if qarr[0]==1:
        print(arr[qarr[1]-1])
    elif qarr[0]==2:
        if qarr[1] in arr:
            print(arr.index(qarr[1])+1)
        else:
            print(0)
    elif qarr[0]==3:
        for i in range(qarr[1]-1,qarr[2]):
            print(arr[i],end=' ')
        print()
