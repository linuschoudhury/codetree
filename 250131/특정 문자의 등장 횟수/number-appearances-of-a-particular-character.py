word=input()
countee=0
counteb=0
for i in range(len(word)-1):
    if word[i]+word[i+1]=='ee':
        countee+=1
    if word[i]+word[i+1]=='eb':
        counteb+=1
print("%d %d"%(countee,counteb))
