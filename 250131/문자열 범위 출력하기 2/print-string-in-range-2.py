word=input()
n=int(input())
for i in range(len(word)-1,len(word)-n-1,-1):
    print(word[i],end='')
