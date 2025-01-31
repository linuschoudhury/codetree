arr=list(input().split())
char=arr[1]
word=arr[0]
pos=-1
for i in range(len(word)):
    if word[i]==char:
        pos=i
        break
if pos==-1:
    print('No')
else:
    print(pos)