word=input()
word=list(word)
a=word[0]
b=word[1]
for i in range(len(word)):
    if word[i]==b:
        word[i]=a
word=''.join(word)
print(word)