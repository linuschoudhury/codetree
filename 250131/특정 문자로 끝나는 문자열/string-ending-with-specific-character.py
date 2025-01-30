arr=[]
for i in range(11):
    word=input()
    arr.append(word)
for i in range(10):
    if arr[i][-1]==arr[-1]:
        print(arr[i])