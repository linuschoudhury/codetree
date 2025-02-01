word=input()
for char in word:
    if 'a'<=char<='z':
        print(char.upper(),end='')
    else:
        print(char.lower(),end='')