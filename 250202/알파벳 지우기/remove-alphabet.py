a=input()
b=input()
numa=numb=''
for char in a:
    if '0'<=char<='9':
        numa+=char
for char in b:
    if '0'<=char<='9':
        numb+=char
print(int(numa)+int(numb))