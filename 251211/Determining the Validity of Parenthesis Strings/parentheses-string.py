str = input()

# Please write your code here.
s=[]
valid=True
for i in range(len(str)):
    if len(s)==0:
        if str[i]=='(':
            s.append(str[i])
        else:
            valid=False
    else:
        if str[i]=='(':
            s.append(str[i])
        else:
            s.pop()
if len(s)==0 and valid==True:
    print('Yes')
else:
    print('No')

