a,b=input().split()
suma=sumb=0
arr1=[]
arr2=[]
for char in a:
    if '0'<=char<='9':
        char=int(char)
        arr1.append(char)
    else:
        break
for i in range(len(arr1)):
    suma=(suma*10)+arr1[i]

for char in b:
    if '0'<=char<='9':
        char=int(char)
        arr2.append(char)
    else:
        break
for i in range(len(arr2)):
    sumb=(sumb*10)+arr2[i]
print(suma+sumb)