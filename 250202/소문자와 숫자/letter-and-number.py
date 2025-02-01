word=input()
for char in word:
    if 'a'<=char<='z' or 'A'<=char<='Z' or '0'<=char<='9':
        print(char.lower(),end='')