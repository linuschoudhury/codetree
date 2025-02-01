word=input()
for char in word:
    if 'A'<=char<='Z':
        print(char,end='')
    elif 'a'<=char<='z':
        print(char.upper(),end='')