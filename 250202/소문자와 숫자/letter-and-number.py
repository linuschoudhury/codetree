word=input()
for char in word:
    if 'a'<=char<='z' or 'A'<=char<='Z' or '1'<=char<='9':
        print(char.lower(),end='')