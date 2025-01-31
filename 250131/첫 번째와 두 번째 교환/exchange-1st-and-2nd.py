word=input()
a=word[0]
b=word[1]
word=list(word)

for i in range(len(word)):
    if word[i]==a:
        word[i]=b
    elif word[i]==b:
        word[i]=a

word=''.join(word)
print(word)