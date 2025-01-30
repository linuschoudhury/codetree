word=input()
arr=[]
for i in range(len(word)):
    if i%2!=0:
        arr.append(word[i])
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end='')