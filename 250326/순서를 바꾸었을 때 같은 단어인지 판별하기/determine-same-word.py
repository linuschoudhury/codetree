word1 = input()
word2 = input()

# Please write your code here.
arr1=list(word1)
arr2=list(word2)
if len(arr1)==len(arr2):
    if arr1.sort()==arr2.sort():
        print('Yes')
    else:
        print('No')
else:
    print('No')