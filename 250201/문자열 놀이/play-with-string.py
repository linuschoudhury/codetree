arr=input().split()
word=arr[0]
n=int(arr[1])

for i in range(n):
    word=list(word)
    arr2=input().split()
    
    num=int(arr2[0])
    
    if num==1:
        a=int(arr2[1])
        b=int(arr2[2])
        
        temp=word[a-1]
        word[a-1]=word[b-1]
        word[b-1]=temp
        
    elif num==2:
        a=arr2[1]
        b=arr2[2]
        for i in range(len(word)):
            if word[i]==a:
                word[i]=b
    word=''.join(word)
    print(word)
    