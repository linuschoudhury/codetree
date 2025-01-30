word1=input()
word2=input()
#n=len(word1)+len(word2)
for i in range(len(word1)):
    if word1[i]!=' ':
        print(word1[i],end='')
for i in range(len(word2)):
    if word2[i]!=' ':
        print(word2[i],end='')