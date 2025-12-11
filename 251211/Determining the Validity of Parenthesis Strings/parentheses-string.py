str = input()

# Please write your code here.
s=[]

for i in range(len(str)):
    if len(s)==0:
        if str[i]=='(':
            s.append(str[i])
    else:
        if str[i]=='(':
            s.append(str[i])
        else:
            s.pop()
if len(s)==0:
    print('Yes')
else:
    print('No')

