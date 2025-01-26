for i in range(5):
    arr=input().split()
    #print(arr)
    for j in range(len(arr)):
        print(chr(ord(arr[j])-32),end=' ')
    print()