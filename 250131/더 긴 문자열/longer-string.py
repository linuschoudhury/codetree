word1,word2=input().split()
if len(word1)>len(word2):
    print("%s %d"%(word1,len(word1)))
elif len(word2)>len(word1):
    print("%s %d"%(word2,len(word2)))
else:
    print('same')
