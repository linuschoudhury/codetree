n=int(input())
total=0
a=0
for i in range(n):
    word=input()
    total+=len(word)
    if word[0]=='a':
        a+=1
print(total,end=' ')
print(a)

