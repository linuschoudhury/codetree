word=input()
char=input()
count=0
for i in range(len(word)):
    if word[i]==char:
        count+=1
print(count)