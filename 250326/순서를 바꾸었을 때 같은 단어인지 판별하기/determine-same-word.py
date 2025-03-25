word1 = input()
word2 = input()

# Please write your code here.
arr1=list(word1)
arr2=list(word2)
arr1.sort()
arr2.sort()
flag=True
if len(arr1)==len(arr2):
    for i in range(len(arr1)):
        if arr1[i]!=arr2[i]:
            flag=False
else:
    flag=False
if flag==True:
    print('Yes')
else:
    print('No')