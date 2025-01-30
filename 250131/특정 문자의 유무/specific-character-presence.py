word=input()
flagab=False
flagee=False
for i in range(len(word)-1):
    if word[i]+word[i+1]=='ee':
        flagee=True
if flagee==True:
    print('Yes',end=' ')
else:
    print('No',end=' ')

for i in range(len(word)-1):
    if word[i]+word[i+1]=='ab':
        flagab=True
if flagab==True:
    print('Yes',end=' ')
else:
    print('No',end=' ')

