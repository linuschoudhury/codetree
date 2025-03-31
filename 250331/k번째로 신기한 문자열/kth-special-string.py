arr1 = input().split(' ')

arraylength=int(arr1[0])

# Please write your code here.
arr2=[]
for i in range(arraylength):
    word=input()
    if word.startswith(arr1[2]):
        arr2.append(word)
arr2.sort()
#print(arr2)
print(arr2[int(arr1[1])-1])

 
